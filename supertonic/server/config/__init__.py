import os
from pathlib import Path

from pydantic_settings import BaseSettings


SUPERTONIC_SERVER_ROOT = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
  SINK_DIR:Path
  

class DevSettings(Settings):
  SINK_DIR:Path = SUPERTONIC_SERVER_ROOT / 'output'

  class Config:
    env_file = 'supertonic/server/config/dev.env'


class BetaSettings(Settings):
  SINK_DIR: Path = Path('/app/output')

  class Config:
    env_file = 'supertonic/server/config/beta.env'


class FactorySettings:
  @staticmethod
  def load():
    env = os.getenv('ENV', 'dev')
    if env == 'beta':
      return BetaSettings()
    else:
      return DevSettings()
    
setting = FactorySettings.load()
print(setting.model_dump_json())