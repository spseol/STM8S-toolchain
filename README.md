STM8 (SPŠE) toolchain
==============================

* Toto je startovací strom zdrojových kódů a `Makefile` pro výuku Mikroprocesorové
  techniky
  s [STM8S](https://www.st.com/en/microcontrollers-microprocessors/stm8s-series.html).
* Strom je určen pro překladač [SDCC](http://sdcc.sourceforge.net/) (nebo 
  [SDCC-gas](https://github.com/XaviDCR92/sdcc-gas)).
* Standardní knihovna pro práci s periferiemi 
  [SPL](https://www.st.com/content/st_com/en/products/embedded-software/mcu-mpu-embedded-software/stm8-embedded-software/stsw-stm8069.html)
  *by se měla* (z licenčních důvodů) stáhnou zvlášť ze stránek výrobce a použít
  [patch](https://github.com/gicking/STM8-SPL_SDCC_patch). Ala myslím, že když napíšete
  `make spl` že to nebude hřích.
* Konkurence a inspirace: \
  * <https://gitlab.com/wykys/stm8-tools>
  * <https://github.com/matejkrenek/stm8-toolchain>

Tři mejkfaily ....
------------------------------------

K dispozici jsou celkem tři `Makefile` v adresáři `.make`. Je to proto, že kompilátor
`SDCC` nedokáže odstranit mrtvý kód. Existují asi tři řešení. To první je
nejoptimálnější, další dvě řešení jsem tu nechal pro strýčka příhodu. Když
poprve zavoláte `make` přepne se toolchain do tohoto nejoptimálnějšího řešení zvaného
`sdcc`.

Mezi jednotlivými `Makefile` se můžete přepínat:

    make switch-sdcc
    make switch-sdcc-gas
    make switch-sdccrm

Přepnutí jen znamená, že se udělá symlink do root-adresáře projektu. Na divných
systémech, které symlinky neumí (například Windows) se natvrdo kopíruje, takže
tato operace může být ztrátová. Na normálních systémech (asi všechny, kromě
Windows) je tato operace bezztrátová.

Pro více detailů se podívejte na
<https://chytrosti.marrek.cz/stm8oss.html>


Použití
--------------

Nejprve je třeba v `Makefile` správně nastavit µprocesor a jeho frakvenci;
případně cestu k instalaci SDCC
[STVP](https://www.st.com/en/development-tools/stvp-stm8.html).

```make
#DEVICE_FLASH=stm8s103f3
DEVICE_FLASH=stm8s208rb

### STlink version for falsh2 targer (stm8flash program)
#STLINK=stlinkv2
#STLINK=stlink
STLINK=stlinkv21

F_CPU=16000000

ifeq ($(OS),Windows_NT)
	CC_ROOT = "/c/Program Files/SDCC"
	STVP_ROOT = "/c/Program Files (x86)/STMicroelectronics/st_toolset/stvp"
else
	CC_ROOT = /usr
endif
```

... no a potom už jen bastlíte, programujete a voláte `make`.

| příkaz&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||
|:---------- |:--------------------------- |
| `make spl` | stáhne a nachystá knihovny |
| `make` | provede kompilaci |
| `make flash` | nahraje program do chipu. Na Linuxu se použije [OpenOCD](https://openocd.org/). Na Windows se použije [STVP](https://www.st.com/en/development-tools/stvp-stm8.html) verze pro příkazový řádek.|
| `make flash2` | záložní varianta, protože OpenOCD někdy nechce čip naprogramovat (používá [stm8flash](https://github.com/vdudouyt/stm8flash)).
| `make clean` | smaže všechno, co nakompiloval
| `make rebuild` | smaže vše a znovu zkompiluje
| `make openocd` | pustí `openocd` pro debug
| `make debug` | spustí STM8-gdb


Závislosti
---------------

* [GNU Make](https://www.gnu.org/software/make/)
* [GNU Bash](https://www.gnu.org/software/bash/) -- ten se na Windows
  dá nainstalovat společně s [Git](https://git-scm.com/download/win)em.
* [SDCC](http://sdcc.sourceforge.net/)
  nebo [SDCC-gas](https://github.com/XaviDCR92/sdcc-gas)
* [STM8 binutils](https://stm8-binutils-gdb.sourceforge.io) (`stm8-gdb`, `stm8-ln`)
* [OpenOCD](https://openocd.org/) pro `flash` a `debug`
  nebo [STVP](https://www.st.com/en/development-tools/stvp-stm8.html)
  pro `flash` na Windows.
* ([stm8flash](https://github.com/vdudouyt/stm8flash) pro `flash2`)

### Na Windows

[`choco`](https://chocolatey.org/)` install git make vscode mingw`

