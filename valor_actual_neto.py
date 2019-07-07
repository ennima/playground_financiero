import os

def VAN_flujos(inversion1,flujos_Arr,rentabilidad):
	#Valor Actual Neto(VAN) o Valor Presente Neto(VPN)

	I_inversion_momento_inicial = inversion1

	# Cada flujo de caja es la diferencia entre Cobros - Pagos
	F_flujos_por_periodo = flujos_Arr
	n_numero_periodos_tiempo = len(F_flujos_por_periodo)
	k_interes_exigido_inversion = rentabilidad

	step1 = I_inversion_momento_inicial * -1
	print("step1:", step1)
	for n in range(1,n_numero_periodos_tiempo + 1):
		
		uno_mas_k_a_la_t = (1 + k_interes_exigido_inversion)**n
		
		print("uno_mas_k_a_la_t:",uno_mas_k_a_la_t)
		stepn = F_flujos_por_periodo[n-1] / uno_mas_k_a_la_t
		

		print("	",F_flujos_por_periodo[n-1],"					",F_flujos_por_periodo[n-1])
		print("------------",n,"----", " = ", "--------------------")
		print(" (1 + ",k_interes_exigido_inversion,")", "   		", uno_mas_k_a_la_t)
		print("=",stepn)
		print(step1," + ", stepn ,"= ")

		step1 += stepn
		print("Queda:", step1,"\n")
	print("VAN:",step1)
	return(step1)

def VAN_flujos_clean(inversion1,flujos_Arr,rentabilidad):
	#Valor Actual Neto(VAN) o Valor Presente Neto(VPN)

	I_inversion_momento_inicial = inversion1

	# Cada flujo de caja es la diferencia entre Cobros - Pagos
	F_flujos_por_periodo = flujos_Arr
	n_numero_periodos_tiempo = len(F_flujos_por_periodo)
	k_interes_exigido_inversion = rentabilidad

	step1 = I_inversion_momento_inicial * -1

	for n in range(1,n_numero_periodos_tiempo + 1):
		
		uno_mas_k_a_la_t = (1 + k_interes_exigido_inversion)**n		
		stepn = F_flujos_por_periodo[n-1] / uno_mas_k_a_la_t
		step1 += stepn

	return(step1)


def VAN_cobro_pago(inversion1,cobros_arr,pagos_arr,rentabilidad):
	#Valor Actual Neto(VAN) o Valor Presente Neto(VPN)

	I_inversion_momento_inicial = inversion1

	# Cada flujo de caja es la diferencia entre Cobros - Pagos
	
	n_numero_periodos_tiempo = len(cobros_arr)
	k_interes_exigido_inversion = rentabilidad

	step1 = I_inversion_momento_inicial * -1
	print("step1:", step1)
	for n in range(1,n_numero_periodos_tiempo + 1):
		
		flujo_n = cobros_arr[n-1] - pagos_arr[n-1]


		uno_mas_k_a_la_t = (1 + k_interes_exigido_inversion)**n
		
		print("uno_mas_k_a_la_t:",uno_mas_k_a_la_t)
		stepn = flujo_n / uno_mas_k_a_la_t
		

		print("	",flujo_n,"					",flujo_n)
		print("------------",n,"----", " = ", "--------------------")
		print(" (1 + ",k_interes_exigido_inversion,")", "   		", uno_mas_k_a_la_t)
		print("=",stepn)
		print(step1," + ", stepn ,"= ")

		step1 += stepn
		print("Queda:", step1,"\n")
	print("VAN:",step1)
	return(step1)


# ejemplo de: https://economipedia.com/definiciones/valor-actual-neto.html
#  validado con: https://es.calcuworld.com/calculadoras-empresariales/calculadora-van/?utm_source=economiasimple.net&utm_medium=Network&utm_campaign=post_link
# VAN_flujos(5000,[1000,2000,2500,3000],0.03)
VAN_cobro_pago(5000,[1000,2000,2500,3000],[0,0,0,0],0.03)


# ejemplo de: https://claseejecutiva.emol.com/articulos/tomas-reyes/calcular-valor-presente-vp-valor-actual-neto-van/
# print(VAN_flujos_clean(60,[-5,4.8,4.8,90],0.1))