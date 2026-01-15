#include "pico/stdlib.h"
#include "hardware/spi.h"
#include "hardware/gpio.h"

#define SPI_PORT_Pi4 spi1
#define PIN_SCK_Pi4   10
#define PIN_MOSI_Pi4  11
#define PIN_MISO_Pi4  12
#define PIN_CS_Pi4    13
#define MSG_LEN 16 //16 byte message

#define SPI_PORT_LORA spi0 
#define PIN_SCK_LORA  18
#define PIN_MOSI_LORA 19
#define PIN_MISO_LORA 16
#define PIN_CS_LORA   17

struct SPI_TX_DATA { //may want to change these to something smaller than floats
    float magx;
    float magy;
    float magz;
    float temp; //if we want to check enclosure temperature
};

struct SPI_RX_DATA { //cleanest way to store incoming tec data
    uint8_t hour;
    uint8_t min;
    uint8_t sv;
    float vert_tec;
    float extra;
    uint8_t flags;
    uint8_t pad[4] = {0,0,0,0};
};

//function declarations
void SPI_SETUP();
SPI_RX_DATA SPI_Pi(SPI_TX_DATA TX_data);

SPI_TX_DATA readSensors();
void updateLoRa(SPI_RX_DATA RX_data);
void updateOLED(SPI_RX_DATA RX_data);

int main() {

    //non-blocking time accumulator
    const uint64_t transmit_interval = 30000; //30 seconds
    uint64_t last_transmit = 0; //start when the program begins reference point
    uint64_t now = 0;

    stdio_init_all(); //good for debugging
    SPI_SETUP();

    while(true){
        SPI_TX_DATA TX_data = readSensors();
        SPI_RX_DATA RX_data = SPI_Pi(TX_data); //full-duplex function sends and returns concurrently
        //OLED and LoRa tranmission
        now = time_ms_64(); // https://sourcevu.sysprogs.com/rp2040/picosdk/symbols/time_us_64
        if((now - last_transmit) > transmit_interval){ //non-blocking way to count time, update every 30 seconds
            updateLoRa(RX_data);
            updateOLED(RX_data);
            last_transmit = now; //update the timer to make if condition false
        } 
    }
}

void SPI_SETUP(){
    // SPI pins for Pi4B on SPI bus 1
    gpio_set_function(PIN_SCK_Pi4,  GPIO_FUNC_SPI);
    gpio_set_function(PIN_MOSI_Pi4, GPIO_FUNC_SPI);
    gpio_set_function(PIN_MISO_Pi4, GPIO_FUNC_SPI);
    gpio_set_function(PIN_CS_Pi4,   GPIO_FUNC_SPI);
    // Init SPI in SLAVE mode
    spi_init(SPI_PORT_Pi4, 1 * 1000 * 1000); // clock ignored in slave
    spi_set_slave(1, true);

    // SPI pins for LoRa on SPI bus 0, default it is master
    gpio_set_function(PIN_SCK_LORA,  GPIO_FUNC_SPI);
    gpio_set_function(PIN_MOSI_LORA, GPIO_FUNC_SPI);
    gpio_set_function(PIN_MISO_LORA, GPIO_FUNC_SPI);
    gpio_set_function(PIN_CS_LORA,   GPIO_FUNC_SPI);
    //Init SPI in Master mode
    spi_init(SPI_PORT_LORA,8000000); //8 MHz, 10MHz is max for the SX1276 https://cdn-shop.adafruit.com/product-files/3179/sx1276_77_78_79.pdf
}

SPI_RX_DATA SPI_Pi(SPI_TX_DATA TX_data){ //this function receives from the master
    SPI_RX_DATA RX_data{}; //all fields set to 0, protecting against partial writes
    uint8_t tx_buf[MSG_LEN] = {0};
    uint8_t rx_buf[MSG_LEN] = {0};

    //store TX_data in TX_buffer to ensure 16 bytes
    memcpy(&tx_buf[0], &TX_data.magx,4);
    memcpy(&tx_buf[4], &TX_data.magy,4);
    memcpy(&tx_buf[8], &TX_data.magz,4);
    memcpy(&tx_buf[12], &TX_data.temp,4);

    spi_write_read_blocking(SPI_PORT_Pi4,tx_buf,rx_buf,MSG_LEN); //(port_used,tx_message,rx_message,length)

    //store received into RX_data
    RX_data.hour = rx_buf[0];
    RX_data.min = rx_buf[1];
    RX_data.sv = rx_buf[2];
    memcpy(&RX_data.vert_tec, &rx_buf[3],4); //(destination, source, number of bytes), this function enables multi-byte values to be stored properly
    memcpy(&RX_data.extra, &rx_buf[7],4);
    RX_data.flags = rx_buf[11]; //need to make a check here for master status on the OLED and LoRa
    memcpy(&RX_data.pad, &rx_buf[12],4);

    return RX_data;
}

//readSensors calculates magnetometer data and temperature data from pins and returns a TX-data struct
SPI_TX_DATA readSensors(){
    SPI_TX_DATA TX_data;
    //read all sensors from pins such as mag an maybe temp? Store into TX_data struct


    return TX_data;
}

void updateLoRa(SPI_RX_DATA RX_data){
    //SPI Protocol
}

void updateOLED(SPI_RX_DATA RX_data){
    //I2C Protocol
}
