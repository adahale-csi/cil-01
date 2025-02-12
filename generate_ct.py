data = ZEISSDataReader(filename).read()
data = TransmissionAbsorptionConverter()(data)
recon = FDK(data).run()
show2D(recon)
