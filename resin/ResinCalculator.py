import datetime
import pytz

def CalculaResina(hora, resin_atual, resin):
  dif = abs(resin - resin_atual)
  result = dif * 8
  hora += datetime.timedelta(minutes=result)
  return "{:02d}:{:02d}".format(hora.hour, hora.minute)

def verifyValue(value):
  value = int(value)
  if value > 160:
    value = 160
  if(value < 0):
    value = 0
  return value

def resinCalculator(resin_atual, resin):
  resin_atual = verifyValue(resin_atual)
  resin = verifyValue(resin)

  if resin_atual > resin:
    return '99:99'

  timezone = pytz.timezone('America/Recife')
  hora_atual = datetime.datetime.now(timezone)
  return CalculaResina(hora_atual, resin_atual, resin)
