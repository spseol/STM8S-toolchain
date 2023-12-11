/*
 * Soubor:  daughterboard.h
 * Datum:   21.11.2023 19:04
 * Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
 * Licence: GNU/GPL 
 * Úloha: 
 * Popis:   hlavičkový soubor pro daughterboard.c
 */

#ifndef __DAUGHTERBOARD_H__
#define __DAUGHTERBOARD_H__

/*  ----      LED      ----     */
#define LED1_PORT GPIOG
#define LED1_PIN GPIO_PIN_0
#define LED2_PORT GPIOG
#define LED2_PIN GPIO_PIN_1
#define LED3_PORT GPIOG
#define LED3_PIN GPIO_PIN_2
#define LED4_PORT GPIOG
#define LED4_PIN GPIO_PIN_3
#define LED5_PORT GPIOG
#define LED5_PIN GPIO_PIN_4
#define LED6_PORT GPIOG
#define LED6_PIN GPIO_PIN_5
#define LED7_PORT GPIOG
#define LED7_PIN GPIO_PIN_6
#define LED8_PORT GPIOG
#define LED8_PIN GPIO_PIN_7

/*  ----      Driver      ----     */
#define SDI_PORT GPIOC
#define SDI_PIN GPIO_PIN_6
#define CLK_PORT GPIOC
#define CLK_PIN GPIO_PIN_5
#define OE_PORT GPIOD
#define OE_PIN GPIO_PIN_0
#define LATCH_PORT GPIOC
#define LATCH_PIN GPIO_PIN_4

#define S1_PORT GPIOB
#define S1_PIN GPIO_PIN_2
#define S2_PORT GPIOB
#define S2_PIN GPIO_PIN_3
#define S3_PORT GPIOB
#define S3_PIN GPIO_PIN_4

// RGB LED
#define PWM_B_PORT GPIOD
#define PWM_B_PIN  GPIO_PIN_4
#define PWM_G_PORT GPIOD
#define PWM_G_PIN  GPIO_PIN_3
#define PWM_R_PORT GPIOA
#define PWM_R_PIN  GPIO_PIN_3

// ADC
#define VREF_PORT GPIOF
#define VREF_PIN GPIO_PIN_7
#define VTEMP_PORT GIPOF
#define VTEMP_PIN GPIO_PIN_6
#define CHANNEL_VREF  ADC2_CHANNEL_15      // 2496 mV
#define CHANNEL_VTEMP ADC2_CHANNEL_14


#endif

