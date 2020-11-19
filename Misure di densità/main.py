import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import Misure as me

#  Definizione della funzione di fit


def line(x, m, q):

    return m * x + q

#  Trovo il best-fit e la matrice di convarianza


popt_acqua, pcov_acqua = curve_fit(line, me.m_acqua, me.h_acqua)
mhat_acqua, qhat_acqua = popt_acqua
sigma_mhat_acqua, sigma_qhat_acqua = np.sqrt(pcov_acqua.diagonal())

popt_olio, pcov_olio = curve_fit(line, me.m_olio, me.h_olio)
mhat_olio, qhat_olio = popt_olio
sigma_mhat_olio, sigma_qhat_olio = np.sqrt(pcov_olio.diagonal())

#  Disegno il grafico cone le misure sperimentali e il loro errore

plt.figure('Grafico massa-altezza')
plt.errorbar(me.m_acqua, me.h_acqua, me.sigma_h_acqua, me.sigma_m_acqua, fmt='.')
plt.errorbar(me.m_olio, me.h_olio, me.sigma_h_olio, me.sigma_m_olio, fmt='.')
plt.xlabel('Massa [g]')
plt.ylabel('Altezza [cm]')
plt.grid(ls='dashed')

# Inserisco il grafico del fit

x = np.linspace(0., 300, 100)
plt.plot(x, line(x, mhat_acqua, qhat_acqua), color = "blue", label = 'Acqua')
plt.plot(x, line(x, mhat_olio, qhat_olio), color = "red", label = 'Olio')


D_acqua = 1/(np.pi * (me.d/2)**2 * mhat_acqua)
sigma_D_acqua = D_acqua* np.sqrt(sigma_mhat_acqua**2/ mhat_acqua + 2*(me.rriga/2)**2 / (me.d/2))

D_olio = 1/(np.pi * (me.d/2)**2 * mhat_olio)
sigma_D_olio = D_olio* np.sqrt(sigma_mhat_olio**2/ mhat_olio + 2*(me.rriga/2)**2 / (me.d/2))

print(f'Densità acqua = {D_acqua} +/- {sigma_D_acqua}')
print(f'Densità olio = {D_olio} +/- {sigma_D_olio}')
print(mhat_acqua, sigma_mhat_acqua)
print(mhat_olio, sigma_mhat_olio)
print(qhat_acqua, sigma_qhat_acqua)
print(qhat_olio, sigma_qhat_olio)



plt.show()
