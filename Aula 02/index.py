'''Bateria em Python'''
import psutil
'''Acesso ao sensor da bateria'''
bateria = psutil.sensors_battery()
'''Captura/solicito o percentual de bateria'''
percentual = str(bateria.percent)
'''Apresenta o nivel'''
print(f'No momento você tem {percentual}% de bateria')

