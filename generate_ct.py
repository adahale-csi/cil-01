data = ZEISSDataReader(raw_x-ray_image-02.tif).read()
data = TransmissionAbsorptionConverter()(data)
recon = FDK(data).run()
show2D(recon)
