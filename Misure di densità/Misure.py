import numpy as np

rbilancia = 2  # Risoluzione della bilancia [g]
rriga = 0.1  # Risoluzione della riga [cm]

# sigma_XX rappresenta l'incertezza della misura corrispondente

tara_acqua = 350          # [g]
d = 8.                                                                # Diametro del cilindro [cm]
sigma_d = rriga

h_acqua = np.array([4.5, 5.7, 6.6, 7.4, 8.6])                         # Altezza dell'acqua [cm]
sigma_h_acqua = np.full(h_acqua.shape, rriga)

m_acquatara = np.array([352, 408, 454, 498, 558])

m_acqua = m_acquatara - np.full(m_acquatara.shape, tara_acqua)        # Massa dell'acqua [g]
sigma_m_acqua = np.full(m_acqua.shape, 2*rbilancia)

################
tara_olio = 350
h_olio = np.array([4.5, 5.4, 6.4, 7.2, 8.9 ])                          # Altezza dell' olio [cm]
sigma_h_olio = np.full(h_olio.shape, rriga)

m_oliotara = np.array([352., 390., 436., 496., 554. ])

m_olio = m_oliotara - np.full(m_oliotara.shape, tara_olio)            # Massa del' olio [g]
sigma_m_olio = np.full(m_olio.shape, 2*rbilancia)









