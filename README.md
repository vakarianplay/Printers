>![](https://img.shields.io/badge/version-python%203.7-blue)
>![](https://img.shields.io/badge/pip%20install-pysnmp-blue)
>![](https://img.shields.io/badge/pip%20install-struct-blue)
>![](https://img.shields.io/badge/pip%20install-Tkinter-blue)

# SNMP printer status

Checking the remaining toner level in printers. Works under the SNMP protocol. The data is displayed in tabular form in a graphical interface via Tkinter.

-------------------
>![](https://img.shields.io/badge/compatible-HP%20LaserJet-success)
>![](https://img.shields.io/badge/compatible-HP%20DesktopJet-success)
>![](https://img.shields.io/badge/compatible-Kyocera-success)
>![](https://img.shields.io/badge/compatible-Brother-success)
>![](https://img.shields.io/badge/compatible-Xerox-success)

## Oid code for toner level.

For Hp printers snmp_oid _1.3.6.1.2.1.43.11.1.1.9.1.1_ return toner level in percent.

For Xerox, Kyocera, Brother snmp_oid _1.3.6.1.2.1.43.11.1.1.9.1.1_ return number of pages printed. Snmp_oid _1.3.6.1.2.1.43.11.1.1.8.1.1_ return maximum cartridge capacity.

### For color printers:
> snmp_oid _1.3.6.1.2.1.43.11.1.1.9.1.1_ return ![](https://img.shields.io/badge/black%20toner%20level-000000)

> snmp_oid _1.3.6.1.2.1.43.11.1.1.9.1.2_ return ![](https://img.shields.io/badge/cyan%20toner%20level-00FFFF)

> snmp_oid _1.3.6.1.2.1.43.11.1.1.9.1.3_ return ![](https://img.shields.io/badge/maganeta%20toner%20level-800080)

> snmp_oid _1.3.6.1.2.1.43.11.1.1.9.1.3_ return ![](https://img.shields.io/badge/yellow%20toner%20level-FFD700)


---------------------------------

![](http://woa.aiq.ru/temp/toner_mon.png)

![](http://woa.aiq.ru/temp/tonermon_set.png)
