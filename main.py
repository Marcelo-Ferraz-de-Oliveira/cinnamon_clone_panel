#Quantos monitores: xrandr -d :0 -q | grep ' connected' | wc -l
#Dump da config: dconf dump /org/cinnamon/
# sudo apt install libcairo2-dev libgirepository1.0-dev
# echo $XDG_CURRENT_DESKTOP == X-Cinnamon

#TODO: painel adicionado iniciando com 90 (1->91, 2->92, etc)
#TODO: identificar os paineis existentes e escolher qual clonar para todos os monitores
#TODO: fazer com rust pra virar pacote, pegar dependências...
#TODO: fazer backup do ~/.cinnamon/conf antes de aplicar o dconf depois voltar os arquivos
import os
import dconfjson
from pprint import pprint
import ast
import json
desktop = os.getenv('XDG_CURRENT_DESKTOP')
print(desktop)

if desktop == 'X-Cinnamon':
    # os.system('cp -Rf ~/.cinnamon/configs ~/.cinnamon/configs_backup')
    os.system('dconf dump /org/cinnamon/ > dconf.conf')
    dconfjson.json_writer("dconf.conf", dest="dconf.json")
    with open('dconf.json') as f:
        data = json.load(f)
        # pprint(data)
    #

    panels_enabled = ast.literal_eval(data[''][' ']['panels-enabled'])
    
    panels = 3
    monitors = 3
    for panel in range(panels+monitors,panels,-1):
        panels_enabled.append(f'{panels}:{panel-panels}:bottom')
    
    data[''][' ']['panels-enabled'] = str(panels_enabled)
    
    print(panels_enabled)
    pprint(data)


    with open('dconf_save.json','w') as w:
        w.write(json.dumps(data))
    dconfjson.dconf_writer('dconf_save.json', dest='dconf_save.conf')
    os.system('rm dconf.conf')
    os.system('rm dconf.json')
    os.system('rm dconf_save.json')
    os.system('dconf load /org/cinnamon/ < dconf_save.conf')

else:
    print("Not running Cinnamon, quitting now...")