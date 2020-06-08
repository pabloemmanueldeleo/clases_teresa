#importamos el modulo
import pymel.core as pm
#creamos las variables a usar.
lit = []
LG = pm.group(em=True,name='LIT_GRP')
rotacion=0
cantidadDeLuces=22
radioDeTodasLasLuces=20
scalaPersonal=3

for n in range(1,cantidadDeLuces):
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
    pl.setAttr('translateX',radioDeTodasLasLuces)
    #rotamos el transform de la luz en y 90 grados
    pl.setAttr('rotateY',90)
    #Escalamos las luces para que queden parejas
    calculoScala=scalaPersonal
    pl.setAttr('scaleX',calculoScala)
    pl.setAttr('scaleY',calculoScala)
    pl.setAttr('scaleZ',calculoScala)
    #rotamos el grupo temporal su transform en Y por cada vuelta le sumamos la rotacion
    grupoTemporal.setAttr('rotateY',rotacion)
    #Emparento el transform de la luz al grupo maestro principal
    pm.parent( pl, LG )
    #Ahora borramos el grupo temporal para limpiar
    pm.delete(grupoTemporal)
    #Guardamos las luces dentro de la variable lit desde su transfomr
    lit.append([l,pl])
    #Al final le sumamos a la variable rotacion 18 para seguir rotando
    rotacion+= 18