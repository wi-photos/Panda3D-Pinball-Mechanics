import direct.directbase.DirectStart
from math import pi,sin, cos
from direct.gui.OnscreenImage import OnscreenImage
from direct.showbase.DirectObject import DirectObject
from direct.showbase.InputStateGlobal import inputState
from panda3d.core import *
from direct.task import Task
from panda3d.bullet import *
import sys
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
class Game(DirectObject):
  def __init__(self):
    self.score = 0
    self.collCount = 0
    base.setBackgroundColor(1,1,1)
    speed = -10
    base.cam.setPos(0, -20, 11)
    base.cam.setHpr(0,-30,0)
    base.disableMouse()
    alight = AmbientLight('ambientLight')
    alight.setColor(Vec4(10.1, 10.1, 10.1, 10))
    alightNP = render.attachNewNode(alight)
    dlight = DirectionalLight('directionalLight')
    dlight.setDirection(Vec3(1, 1, -1))
    dlight.setColor(Vec4(0.7, 0.7, 0.7, 1))
    dlightNP = render.attachNewNode(dlight)
    render.clearLight()
    render.setLight(alightNP)
    render.setLight(dlightNP)
    render.setShaderAuto
    taskMgr.add(self.update, 'updateWorld')
    self.setup()
  def doExit(self):
    sys.exit(1)
  def downflipper(self):
    self.Flipper1.setHpr(0, 0, 20)
    self.f.setHpr(0, 0, -150)
    self.f.setPos(-1.5, 0, -2.72)
    self.plane.setPos(-0.9, 0, -3.1)
    self.Flipper1.node().setRestitution(0)
  def downflipper2(self):
    self.Flipper2.setHpr(40, 0, -20)
    self.f2.setHpr(0, 0, -30)
    self.f2.setPos(1.5, 0, -2.72)
    self.plane2.setPos(0.9, 0, -3.2)
    self.Flipper2.node().setRestitution(0)
  def handleRailCollision(self, entry):
    print entry
  def doTask(self):
    self.plane.setPos(-0.9, 0, -2.6)
    self.Flipper1.node().setRestitution(0.3)
    self.Flipper1.setHpr(0, 0, -60.5)
    self.f.setHpr(0, 0, 130)
#taskMgr.doMethodLater(0.3, self.downflipper, 'nn')
  def doTask2(self):
    self.Flipper2.setHpr(0, 0, 60)
    self.f2.setHpr(0, 0, 60)
    #self.f2.setPos(1, 0, -1.9)
    self.plane2.setPos(0.9, 0, -2.6)
    self.Flipper2.node().setRestitution(0.3)
  #taskMgr.doMethodLater(0.3, self.downflipper2, 'nn')
  def doReset(self):
    self.cleanup()
    self.setup()
  def toggleWireframe(self):
    base.toggleWireframe()
  def toggleTexture(self):
    base.toggleTexture()
  def toggleDebug(self):
    if self.debugNP.isHidden():
      self.debugNP.show()
    else:
      self.debugNP.hide()
  def doScreenshot(self):
    base.screenshot('Pinball')
  def processContacts(self):
    if not self.Ball.node() or not  self.ob.node():
      return
    result = self.world.contactTestPair(self.Ball.node(),  self.ob.node())
    for contact in result.getContacts():
     cp = contact.getManifoldPoint()
     node0 = contact.getNode0()
     node1 = contact.getNode1()
     self.score = (self.score) + 2
  def processContacts2(self):
    if not self.Ball.node() or not  self.ob2.node():
        return
    result = self.world.contactTestPair(self.Ball.node(),  self.ob2.node())
    for contact in result.getContacts():
     cp = contact.getManifoldPoint()
     node0 = contact.getNode0()
     node1 = contact.getNode1()
     self.score = (self.score) + 2
  def processContacts3(self):
    if not self.Ball.node() or not  self.ob3.node():
        return
    result = self.world.contactTestPair(self.Ball.node(),  self.ob3.node())
    for contact in result.getContacts():
     cp = contact.getManifoldPoint()
     node0 = contact.getNode0()
     node1 = contact.getNode1()
     self.score = (self.score) + 10
  def update(self, task):
    dt = globalClock.getDt()
    self.world.doPhysics(dt, 10, 1.0/180.0)
    self.processContacts()
    self.processContacts2()
    self.processContacts3()
    self.scorelabel['text'] = str(self.score)
#self.scorelabel['fg'] = (1,0,0)
    return task.cont
  def restart(self):
    self.Ball.setPos(1.8, 0, 2)
    self.score = 0
  def setup(self):
    self.scorelabel = DirectLabel()
    self.scorelabel.reparentTo(render)
    self.scorelabel.setPos(4,-0.1,4)
    self.scorelabel.setScale(0.5)
    self.score22 = loader.loadModel("models/Plane")
    self.score22.setPos(4, 0, 4)
    self.score22.setScale(2)
#  self.score22.setHpr(0, 0, 30)
    self.score22.reparentTo(render)
    self.f = loader.loadModel("models/flipper")
    self.f.setPos(-1.5, 0, -2.72)
    self.f.setScale(0.3)
    self.f.setHpr(0, 0, -150)
    self.f.reparentTo(render)
    self.f2 = loader.loadModel("models/flipper")
    self.f2.setPos(1.5, 0, -2.72)
    self.f2.setScale(0.3)
    self.f2.setHpr(0, 0, -30)
    self.f2.reparentTo(render)
    self.b = loader.loadModel("models/border")
    self.b.setPos(2.7, 0, -3.2)
    self.b.setScale(1.7,1.15,1.2)
    self.b.setHpr(0, 0, -90)
    self.b.reparentTo(render)
    self.b2 = loader.loadModel("models/border")
    self.b2.setPos(-3.1, 0, -3.2)
    self.b2.setScale(1.7,1.15,1.2)
    self.b2.setHpr(0, 0, -90)
    self.b2.reparentTo(render)
    self.b3 = loader.loadModel("models/border")
    self.b3.setPos(-0.3, 0, 4.8)
    self.b3.setScale(0.6,1.15,1.2)
    self.b3.setHpr(0, 0, -0)
    self.b3.reparentTo(render)
    self.b4 = loader.loadModel("models/border")
    self.b4.setPos(2.3, 0, -2.2)
    self.b4.setScale(0.1,1.15,1.2)
    self.b4.setHpr(0, 0, -20)
    self.b4.reparentTo(render)
    self.b5 = loader.loadModel("models/border")
    self.b5.setPos(-2.3, 0, -2.2)
    self.b5.setScale(0.12,1.15,1.2)
    self.b5.setHpr(0, 0, 20)
    self.b5.reparentTo(render)
    self.w = loader.loadModel("models/Plane")
    self.w.setPos(-0.2, 0.7, -0.3)
    self.w.setScale(6.2,1.15,10.2)
    texw = loader.loadTexture('models/wood.png')
    self.w.setTexture(texw, 1)
    self.w.reparentTo(render)
    resetbutton = DirectButton(text = ("Restart", "Restart", "Restart", "Restart"), scale=.1, command=self.restart)
    resetbutton.setPos(-1.1,0,0.9)
    self.worldNP = render.attachNewNode('World')
    # World
    self.world = BulletWorld()
    self.world.setGravity(Vec3(0, 0, -5.81))
    shape = BulletPlaneShape(Vec3(0, 0, 1), 1)
    self.groundNP = self.worldNP.attachNewNode(BulletRigidBodyNode('Ground'))
    self.groundNP.node().addShape(shape)
    self.groundNP.setPos(0, 0, -14)
    self.groundNP.setCollideMask(BitMask32.allOn())    
    self.world.attachRigidBody(self.groundNP.node())
    #These invisible planes stop the ball from coming towards the camera
    shape5 = BulletPlaneShape(Vec3(0, -2, 0), 1)
    node = BulletRigidBodyNode('Ground')
    node.addShape(shape5)
    np = render.attachNewNode(node)
    np.setPos(0, 1.1, 0)
    self.world.attachRigidBody(node)
    shape6 = BulletPlaneShape(Vec3(0, 2, 0), 1)
    node2 = BulletRigidBodyNode('Ground2')
    node2.addShape(shape6)
    np2 = render.attachNewNode(node2)
    np2.setPos(1, -1.01, 4)
    self.world.attachRigidBody(node2)
    #end of invisible planes
    shape = BulletBoxShape(Vec3(0.5, 0.01, 0.5))
    shape7 = BulletPlaneShape(Vec3(0, 0, 1), 1)
    self.Ball = self.worldNP.attachNewNode(BulletRigidBodyNode('Box'))
    self.Ball.node().setMass(3000)
    self.Ball.node().addShape(shape)
    self.Ball.node().setRestitution(6)
    self.Ball.setPythonTag("velocity", 100000000000.001)
    self.Ball.setPos(1.8, 0, 2)
    self.Ball.setScale(0.3, 0.3, 0.3)
    self.Ball.setCollideMask(BitMask32.allOn())
    #self.Ball.node().setDeactivationEnabled(False)
    self.world.attachRigidBody(self.Ball.node())
    visualNP = loader.loadModel('models/ball')
    visualNP.clearModelNodes()
    visualNP.reparentTo(self.Ball)
    visualNP.setScale(1.5, 1.5, 1.5)
    m = Material()
    m.setSpecular(Vec4(1,1,1,1))
    m.setShininess(96)
    self.Ball.setMaterial(m, 1)
    shape = BulletBoxShape(Vec3(0.4, 1.5, 0.5))
    self.Flipper1 = self.worldNP.attachNewNode(BulletRigidBodyNode('Flipper1'))
    self.Flipper1.node().setMass(0.0)
    self.Flipper1.node().addShape(shape)
    self.Flipper1.node().setRestitution(0)
    self.Flipper1.setPythonTag("velocity", -10000000000000.001)
    self.Flipper1.setPos(-1.3, 0, -2.8)
    self.Flipper1.setHpr(0, 0, 20)
    self.Flipper1.setScale(1.5, 0.5, 0.5)
    self.Flipper1.setCollideMask(BitMask32.allOn())
    self.world.attachRigidBody(self.Flipper1.node())
    shapeo = BulletSphereShape(0.7)
    self.ob = self.worldNP.attachNewNode(BulletRigidBodyNode('ob'))
    self.ob.node().setMass(0.0)
    self.ob.node().addShape(shapeo)
    self.ob.node().setRestitution(0.2)
    self.ob.setPythonTag("velocity", -10000000000000.001)
    self.ob.setPos(-1.3, 0, 2.3)
    self.ob.setHpr(0, 0, 0)
    self.ob.setScale(0.3, 0.3, 0.3)
    self.ob.setCollideMask(BitMask32.allOn())
    self.world.attachRigidBody(self.ob.node())
    self.sphere =  self.ob
    visualNP = loader.loadModel('models/goal2')
    visualNP.clearModelNodes()
    visualNP.reparentTo(self.ob)
    shapeo2 = BulletSphereShape(0.7)
    self.ob2 = self.worldNP.attachNewNode(BulletRigidBodyNode('ob2'))
    self.ob2.node().setMass(0.0)
    self.ob2.node().addShape(shapeo)
    self.ob2.node().setRestitution(0.2)
    self.ob2.setPythonTag("velocity", -10000000000000.001)
    self.ob2.setPos(0.1, 0, 2.3)
    self.ob2.setHpr(0, 0, 0)
    self.ob2.setScale(0.3, 0.3, 0.3)
    self.ob2.setCollideMask(BitMask32.allOn())
    self.world.attachRigidBody(self.ob2.node())
    visualNP = loader.loadModel('models/goal2')
    visualNP.clearModelNodes()
    visualNP.reparentTo(self.ob2)
    self.ob3 = self.worldNP.attachNewNode(BulletRigidBodyNode('ob3'))
    self.ob3.node().setMass(0.0)
    self.ob3.node().addShape(shapeo)
    self.ob3.node().setRestitution(0.2)
    self.ob3.setPythonTag("velocity", -10000000000000.001)
    self.ob3.setPos(-0.7, 0, 3.5)
    self.ob3.setHpr(0, 0, 0)
    self.ob3.setScale(0.3, 0.3, 0.3)
    self.ob3.setCollideMask(BitMask32.allOn())
    self.world.attachRigidBody(self.ob3.node())
    visualNP = loader.loadModel('models/goal2')
    visualNP.clearModelNodes()
    visualNP.reparentTo(self.ob3)
    shapeplane = BulletSphereShape(0.9)
    self.plane = self.worldNP.attachNewNode(BulletRigidBodyNode('plane'))
    self.plane.node().setMass(0.0)
    self.plane.node().addShape(shapeplane)
    self.plane.node().setRestitution(0.4)
    self.plane.setPythonTag("velocity", -10000000000000.001)
    self.plane.setPos(-0.9, 0, -3.1)
    self.plane.setHpr(-40, 0, 20)
    self.plane.setScale(0.5, 110.7, 0.3)
    self.plane.setCollideMask(BitMask32.allOn())
    #self.Ball.node().setDeactivationEnabled(False)
    self.world.attachRigidBody(self.plane.node())
    shapeplanew = BulletSphereShape(0.9)
    self.plane2 = self.worldNP.attachNewNode(BulletRigidBodyNode('plane2'))
    self.plane2.node().setMass(0.0)
    self.plane2.node().addShape(shapeplanew)
    self.plane2.node().setRestitution(0.4)
    self.plane2.setPos(0.9, 0, -3.2)
    self.plane2.setHpr(40, 0, -20)
    self.plane2.setScale(0.5, 110.7, 0.3)
    self.plane2.setCollideMask(BitMask32.allOn())
    #self.Ball.node().setDeactivationEnabled(False)
    self.world.attachRigidBody(self.plane2.node())
    shape = BulletBoxShape(Vec3(0.4, 1.5, 0.5))
    self.Flipper2 = self.worldNP.attachNewNode(BulletRigidBodyNode('Flipper2'))
    self.Flipper2.node().setMass(0.0)
    self.Flipper2.node().addShape(shape)
    self.Flipper2.node().setRestitution(0)
    self.Flipper2.setPythonTag("velocity", -10000000000000000.00)
    self.Flipper2.setPos(1.3, 0, -2.8)
    self.Flipper2.setHpr(40, 0, -20)
    self.Flipper2.setScale(1.5, 0.5, 0.5)
    self.Flipper2.setCollideMask(BitMask32.allOn())
    #self.Ball.node().setDeactivationEnabled(False)
    self.world.attachRigidBody(self.Flipper2.node())
	#Top
    shape = BulletBoxShape(Vec3(10.5, 10.5, 0.5))
    self.topNP = self.worldNP.attachNewNode(BulletRigidBodyNode('Boxx'))
    self.topNP.node().setMass(0.0)
    self.topNP.node().addShape(shape)
    self.topNP.setPos(-0.2, 0, 4.8)
    self.topNP.setScale(6.4, 10.5, 0.3)
    self.topNP.setCollideMask(BitMask32.allOn())
    #self.Ball.node().setDeactivationEnabled(False)
    self.world.attachRigidBody(self.topNP.node())
    tex2 = loader.loadTexture('models/Top.png')
    shapeside2 = BulletBoxShape(Vec3(1.5, 1.5, 1.5))
    shapeside = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
    self.side1 = self.worldNP.attachNewNode(BulletRigidBodyNode('Boxx'))
    self.side1.node().setMass(0.0)
    self.side1.node().addShape(shapeside2)
    self.side1.setPos(-3.4, 0, 0.28)
    self.side1.setScale(0.3, 0.3, 9)
    self.side1.setHpr(0, -10, 0.3)
    self.side1.setCollideMask(BitMask32.allOn())
    #self.Ball.node().setDeactivationEnabled(False)
    self.world.attachRigidBody(self.side1.node())
    #side1
    self.side2 = self.worldNP.attachNewNode(BulletRigidBodyNode('Boxx'))
    self.side2.node().setMass(0.0)
    self.side2.node().addShape(shapeside2)
    self.side2.setPos(3, 0, 0.28)
    self.side2.setScale(0.3, 10, 9)
    self.side2.setHpr(0, -15, 0.3)
    self.side2.setCollideMask(BitMask32.allOn())
    #self.side2.node().setDeactivationEnabled(False)
    self.world.attachRigidBody(self.side2.node())
    tex2 = loader.loadTexture('models/side.png')
    shapesside = BulletBoxShape(Vec3(0.2, 1.1, 0.01))
    self.sside = self.worldNP.attachNewNode(BulletRigidBodyNode('sside'))
    self.sside.node().setMass(0.0)
    self.sside.node().addShape(shapeside)
    self.sside.setHpr(0, -0, 150.3)
    self.sside.setPos(2.4, 0, -2)
    self.sside.setScale(1.4, 1, 0.3)
    self.sside.setCollideMask(BitMask32.allOn())
    #self.Ball.node().setDeactivationEnabled(False)
    self.world.attachRigidBody(self.sside.node())
    tex2 = loader.loadTexture('models/SSide.png')
    shapesside2 = BulletBoxShape(Vec3(0.2, 1.1, 0.01))
    self.sside2 = self.worldNP.attachNewNode(BulletRigidBodyNode('sside'))
    self.sside2.node().setMass(0.0)
    self.sside2.node().addShape(shapeside)
    self.sside2.setHpr(0, -0, -150.3)
    self.sside2.setPos(-2.4, 0, -2)
    self.sside2.setScale(1.6, 1, 0.3)
    self.sside2.setCollideMask(BitMask32.allOn())
    #self.Ball.node().setDeactivationEnabled(False)
    self.world.attachRigidBody(self.sside2.node())
    self.accept('arrow_left',self.doTask)
    #self.accept('arrow_up-up',self.downflipper)
    self.accept('arrow_right',self.doTask2)
    self.accept('arrow_left-up', self.downflipper) # cal
    self.accept('arrow_right-up', self.downflipper2) # cal
    self.accept('escape', sys.exit) # exit on esc
fgame = Game()
run()
