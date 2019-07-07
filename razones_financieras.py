import os

def razon_del_circulante(activo_circulante, pasivo_corto_plazo):
	rc = activo_circulante / pasivo_corto_plazo
	print("razon_del_circulante = ", activo_circulante,"/",pasivo_corto_plazo,"=",rc )
	return rc

def prueba_de_acido(activo_circulante, inventarios, pasivo_corto_plazo):
	pa = (activo_circulante - inventarios) / pasivo_corto_plazo
	print("prueba_de_acido = (",activo_circulante,"-",inventarios,") / ",pasivo_corto_plazo," = ", pa)
	return pa

def rentabilidad_de_lasventas(utilidad_neta, ventas_netas):
	rv = utilidad_neta / ventas_netas
	print("rentabilidad_de_lasventas = ",utilidad_neta,"/",ventas_netas,"=",rv)
	return rv

# http://academica.uaslp.mx/oa/estadoresultados/utilidad_de_operacin.html
# Utilidad de operación = Utilidad Bruta + Gastos de Operación

# https://www.ejemplode.com/46-contabilidad/986-ejemplo_de_utilidad_de_operacion.html
# Utilidad de operación = Utilidad Bruta - Gastos de Operación

# https://www.lifeder.com/utilidad-operacional/#Como_se_calcula
#  Utilidad operacional = ingresos operacionales (ventas) – costo de la mercancía vendida – gastos operacionales – depreciación – amortización
# https://credilike.me/blog/utilidad-bruta-y-utilidad-neta/
#  Utilidad bruta – Gastos operativos = Utilidad operativa
# Ventas netas – Costo de ventas o costos de producción = Utilidad Bruta
# Utilidad operativa – (gastos financieros + impuestos) = utilidad neta

# https://www.gestiopolis.com/cuales-son-las-razones-financieras-de-rentabilidad/
# Margen de utilidad operativa = Utilidad operativa / Ventas
def margen_utilidad_de_operacion(utilidad_de_operacion,ventas):
	muo = utilidad_de_operacion / ventas
	print("margen_utilidad_de_operacion = ",utilidad_de_operacion,"/",ventas,"=",muo)
	return muo



#  Rentabilidad del activo = Utilidad neta/ Activo total.
def rentabilidad_del_activo(utilidad_neta, activo_total):
	ra = utilidad_neta / activo_total
	print("rentabilidad_del_activo = ",utilidad_neta,"/",activo_total," =",ra)
	return ra


# Rentabilidad del capital = Utilidad neta/ Capital contable.
def rentabilidad_del_capital(utilidad_neta, capital_contable):
	rc = utilidad_neta / capital_contable
	print("rentabilidad_del_capital = ",utilidad_neta,"/",capital_contable," =",rc)
	return rc


# 11 651 791 (2018)   , 10237992 (2017)
activo_circulante = 11651791

# $40 809 768 (2018)  ,    $36 838 288  (2017)
activo_total = 40809768

# 10 770 317 (2018)   ,  11 679 872 (2017)
pasivo_corto_plazo = 10770317


# 22 454 910 (2018) , 20 111 154 (2017)
capital_contable = 22454910
# 6 569 959 (2018)    ,  6490434 (2017)
inventarios = 6569959

# $2 534 629 (2018) ,   2289726 (2017)
utilidad_neta =  2534629

#  $50 409 166 (2018),  47567704 (2017)
ventas_netas = 50409166

#  3 215 104 (2018)  ,   2881264 (2017)
utilidad_de_operacion = 3215104 

razon_del_circulante(activo_circulante,pasivo_corto_plazo)
prueba_de_acido(activo_circulante, inventarios, pasivo_corto_plazo)
rentabilidad_de_lasventas(utilidad_neta, ventas_netas)
margen_utilidad_de_operacion(utilidad_de_operacion,ventas_netas)
rentabilidad_del_activo(utilidad_neta, activo_total)
rentabilidad_del_capital(utilidad_neta, capital_contable)