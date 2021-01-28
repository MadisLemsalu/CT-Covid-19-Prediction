
from bentoml import BentoService, api, env, artifacts
from bentoml.artifact import FastaiModelArtifact
from bentoml.adapters import FastaiImageInput
from fastai2.medical.imaging  import *
from fastai2.vision.all import *

@env(pip_dependencies=['fastai'])
@artifacts([FastaiModelArtifact('covid_classifer')])
class PetClassification(BentoService):
    
    @api(input=FastaiImageInput())
    def predict(self, image):
        dcm = image.dcmread()

        result = self.artifacts.covid_classifer.predict(image)
        return str(result)
