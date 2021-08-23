import Augmentor
p = Augmentor.Pipeline(
    "C:\\Users\\Mislab\\Desktop\\medical\\MF\\COVID-CT-master\\Images-processed\\CT_NonCOVID")

p.random_distortion(1, grid_width=10, grid_height=10, magnitude=3)

p.sample(800)
p.process()
