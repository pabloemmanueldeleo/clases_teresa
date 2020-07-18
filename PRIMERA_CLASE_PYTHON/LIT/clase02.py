import pymel.core as pm
import arnold
import math

def ringLight(radio=100,luces=14,pos=(0,0,0),rot=(0,0,0),scala=0):
    lit = []
    LG = pm.group(em=True,name='LIT_RINGLIGHT_GRP')
    rotacion=0
    
    if scala==0:
        scala=radio*math.pi/luces
    else:
        scala=scala
    
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
    
    LG.setAttr('translateX',pos[0])
    LG.setAttr('translateY',pos[1])
    LG.setAttr('translateY',pos[2])
    LG.setAttr('rotateX',rot[0])
    LG.setAttr('rotateY',rot[1])
    LG.setAttr('rotateZ',rot[2])
    
    return lit,LG
    
def crearRing():
    cantidad=pm.textFieldGrp(cant,q=True,text=True)
    radio=pm.textFieldGrp(rad,q=True,text=True)
    p1=pm.floatField(ffp1,q=True,value=True)
    p2=pm.floatField(ffp2,q=True,value=True)
    p3=pm.floatField(ffp3,q=True,value=True)
    r1=pm.floatField(ffr1,q=True,value=True)
    r2=pm.floatField(ffr2,q=True,value=True)
    r3=pm.floatField(ffr3,q=True,value=True)
    #print (int(cantidad),int(radio),p1,p2,p3,r1,r2,r3)
    ringLight(int(radio),int(cantidad),(p1,p2,p3),(r1,r2,r3))
    
wname='LIT RING'

if pm.window('LIT RING',ex=True):
    pm.deleteUI('LIT RING')

window = pm.window('LIT RING',title='LIT RING')
c=pm.columnLayout(adjustableColumn=True)
cant=pm.textFieldGrp( label='Cantidad', text='14' )
rad=pm.textFieldGrp( label='Radio', text='100' )
pm.rowColumnLayout( numberOfColumns=4, columnWidth=[(1, 60), (2, 80), (3, 80)] )
pm.text('Position')
ffp1=pm.floatField( precision=2 )
ffp2=pm.floatField( precision=2 )
ffp3=pm.floatField( precision=2 )
pm.setParent(c)
pm.rowColumnLayout( numberOfColumns=4, columnWidth=[(1, 60), (2, 80), (3, 80)] )
pm.text('Rotacion')
ffr1=pm.floatField( minValue=-360, maxValue=360, precision=2 )
ffr2=pm.floatField( minValue=-360, maxValue=360, precision=2 )
ffr3=pm.floatField( minValue=-360, maxValue=360, precision=2 )
pm.setParent(c)
pm.button('CREAR LIT RING',c='crearRing()',h=100)
window.show()


