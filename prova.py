# -*- coding: utf-8 -*-

import datetime

class Nom:

	# Generem una llista amb les opcions que s'escolliran més tard
	universitat = ['URV', 'UB', 'Pompeu Fabra', 'UVIC']

	def get_data_actual():
		"""Retorna la data actual amb format dd/mm/aaaa"""
		avui = datetime.datetime.now()
		data_actual = avui.strftime("%d/%m/%Y")
		return data_actual

	def comprova_nom(self):
		"""Comprova el nom escrit, si és Jordi saluda, si no diu adeu"""
		if self.nom == "Jordi":
			print "Bon dia Jordi!!"
		else:
			print 'Adéu '+self.nom+' ens veiem aviat!'

	def seleccionar_universitat(self):
		"""Dona les Universitats com opcions a escollir"""
		codi_universitat = 0

		for universitat in self.universitat:
			print '(%d) %s ' % (codi_universitat, universitat)
			codi_universitat = codi_universitat+1

		print'\n'
		escollir_universitat = raw_input('quina esculls?')
		escollir_universitat = int(escollir_universitat)
		self.universitat = self.universitat[escollir_universitat]
		print 'Has escollit: '+self.universitat

	data_actual = get_data_actual()


	def __init__(self):
		print "Hola estic fent una prova\n\tAra mostraré el teu nom i la data actual:"
		self.nom = raw_input('\tCom et dius? ')
		self.comprova_nom()
		print 'La data d\'avui és: '+self.data_actual+'\n'
		print 'Has d\'escollir entre les següents Universitats:'
		self.seleccionar_universitat()

Nom = Nom()
