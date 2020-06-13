import pymel.core as pm
import math
lit = []
LG = pm.group(em=True,name='LIT_GRP')
rotacion=0

radio=200
luces=20

scala=radio*math.pi/luces

for n in range(1,luces+1):
    #Generamos nombre de la luz
    newName='LUZ_{0}_AIAL'.format(str(n).zfill(3))
    #Creamos un grupo para usarlo temporalmente
    grupoTemporal = pm.group(em=True)
    #Creando un nodo de luz arnold area
    l = pm.createNode('aiAreaLight')
    #Pedimos el padre del shape de nuestra luz
    pl = l.getParent()
    #Renombramos el nombre del padre de la luz
    pl.rename(newName)
    #Emparentamos el padre de la luz en el grupo temporal
    pm.parent(pl,grupoTemporal)
    #movemos la el transform de la luz en x positivo 10
    pl.setAttr('translateX',radio)
    #rotamos el transform de la luz en y 90 grados
    pl.setAttr('rotateY',90)
    #rotamos el grupo temporal su transform en Y por cada vuelta le sumamos la rotacion
    grupoTemporal.setAttr('rotateY',rotacion)
    #Escalamos las luces para que queden parejas
    pl.setAttr('scaleX',scala)
    pl.setAttr('scaleY',scala)
    pl.setAttr('scaleZ',scala)
    #Emparento el transform de la luz al grupo maestro principal
    pm.parent( pl, LG )
    #Ahora borramos el grupo temporal para limpiar
    pm.delete(grupoTemporal)
    #Guardamos las luces dentro de la variable lit desde su transfomr
    lit.append([l,pl])
    #Al final le sumamos a la variable rotacion 18 para seguir rotando
    rotacion+= 360/luces