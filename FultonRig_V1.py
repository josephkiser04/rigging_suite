import maya.cmds as cmds
def fulRigWindow():
    title = 'Fulton Rig'
    rigWin = 'rigWindow'

    if cmds.window(rigWin, exists =True):
        cmds.deleteUI(rigWin)
    if cmds.windowPref(rigWin, exists =True):
        cmds.windowPref(rigWin,remove=True)
    mainWindow =cmds.window(rigWin, title=title,wh=(400,250))
    cmds.columnLayout('cNameSpace',adj=True)
    cmds.text(label='Character Name:',align='left')
    characterNameSpace = cmds.textField('characterNameSpace',w=300)
    cmds.separator(h=5)
    cmds.setParent('..')
    ##--Arm--------------
    cmds.tabLayout()
    cmds.columnLayout('Arms',adj=True)
    arms_form = cmds.formLayout(numberOfDivisions=100)
    at1 = cmds.text('at1',label='Prefix:',align='left')
    atf1 = cmds.textField('atf1',w=300)
    at2 = cmds.text('at2',label='Suffix:',align='left')
    atf2 = cmds.textField('atf2',w=300)
    as1 = cmds.separator( 'as1',height=5, style='out' )
    as2 = cmds.separator( 'as2',height=5, style='out' )
    ab1 = cmds.button('ab1',l='Location Joints',c='armLoc()')
    ab2 = cmds.button('ab2', l='Create Rig',c='armCreation()')
    cmds.formLayout(arms_form,e=True,af=[('at1','top',5),('at1','left',5),('atf1','top',5),('as1','top',5),
                                            ('as1','left',5),('at2','top',5),('at2','left',5),('atf2','top',5),
                                            ('as2','left',5),('as2','top',5),('ab1','right',5),('ab2','right',5)],
                                            
                                            
                                    ac=[('atf1','left',5,'at1'),('as1','top',5,'atf1'),('atf2','left',5,'at2'),
                                    ('at2','top',5,'as1'),('atf2','top',5,'as1'),('as2','top',5,'at2'),('ab1','top',5,'as2'),
                                    ('ab2','top',5,'ab1')])
    ##stuff
    cmds.setParent('..')
    cmds.setParent('..')
    ##--------------Legs-----------
    cmds.columnLayout('Legs',adj=True)
    leg_form = cmds.formLayout(numberOfDivisions=100)
    lt1 = cmds.text('lt1',label='Prefix:',align='left')
    ltf1 = cmds.textField('ltf1',w=300)
    lt2 = cmds.text('lt2',label='Suffix:',align='left')
    ltf2 = cmds.textField('ltf2',w=300)
    ls1 = cmds.separator( 'ls1',height=5, style='out' )
    ls2 = cmds.separator( 'ls2',height=5, style='out' )
    lb1 = cmds.button('lb1',l='Location Joints',c='legLoc()')
    lb2 = cmds.button('lb2', l='Create Rig',c='legCreation()')
    cmds.formLayout(leg_form,e=True,af=[('lt1','top',5),('lt1','left',5),('ltf1','top',5),('ls1','top',5),
                                            ('ls1','left',5),('lt2','top',5),('lt2','left',5),('ltf2','top',5),
                                            ('ls2','left',5),('ls2','top',5),('lb1','right',5),('lb2','right',5)],
                                            
                                            
                                    ac=[('ltf1','left',5,'lt1'),('ls1','top',5,'ltf1'),('ltf2','left',5,'lt2'),
                                    ('lt2','top',5,'ls1'),('ltf2','top',5,'ls1'),('ls2','top',5,'lt2'),('lb1','top',5,'ls2'),
                                    ('lb2','top',5,'lb1')])
    ##stuff
    cmds.setParent('..')
    cmds.setParent('..')
    ##------------------------Spine--------
    cmds.columnLayout('Spine',adj=True)
    spine_form = cmds.formLayout(numberOfDivisions=100)
    ## stuff for tabLayout
    rbgS1 = cmds.radioButtonGrp('rbgS1', label='Spine Setups:', labelArray2=['Fk spine', 'Advanced Spine'], numberOfRadioButtons=2,
                                cal=[1,'left'],cl2=['left','left'])
    ##----------------Prefix
    sPFt1 = cmds.text('sPFt1',label='Prefix:',align='left')
    sPFtf1 = cmds.textField('sPFtf1',w=300)
    sSFt1 = cmds.text('sSFt1',label='Suffix:',align='left')
    sSFtf1 = cmds.textField('sSFtf1',w=300)
    sPFs1 = cmds.separator( 'sPFs1',height=5, style='out' )
    sB1 = cmds.button('sB1',l='Locator Joints',c='spineLoc()')
    sB2 = cmds.button('sB2',l='Create Rig',c='spineCreation()')
    ## call form
    cmds.formLayout(spine_form,e=True,af=[('rbgS1','top',5),('rbgS1','left',5),('sPFt1','top',5),('sPFt1','left',5),
                                        ('sPFtf1','top',5),('sPFtf1','left',5),('sSFt1','top',5),('sSFt1','left',5),
                                        ('sSFtf1','top',5),('sSFtf1','left',5),('sPFs1','top',5),('sB1','top',5),
                                        ('sB2','top',5),('sB1','right',5),('sB2','right',5)],
                                    
                                    
                                    ac=[('sPFt1','top',5,'rbgS1'),('sPFtf1','top',5,'rbgS1'),('sPFtf1','left',5,'sPFt1'),
                                    ('sSFt1','top',10,'sPFtf1'),('sSFtf1','top',10,'sPFtf1'),('sSFtf1','left',5,'sSFt1'),
                                    ('sPFs1','top',5,'sSFtf1'),('sB1','top',5,'sPFs1'),('sB2','top',5,'sB1')])

    cmds.setParent('..')
    cmds.setParent('..')
    cmds.columnLayout('Hand',adj=True)
    hand_form = cmds.formLayout(numberOfDivisions=100)
    ## stuff for tabLayout
    hT1 = cmds.text('hT1',l='Preffix:',align='left')
    hTF1 = cmds.textField('hTF1',w=300)
    hT2 = cmds.text('hT2',l='Suffix:',align='left')
    hTF2 = cmds.textField('hTF2',w=300)
    hS1 = cmds.separator( 'hS1',height=5, style='out' )
    hB1 = cmds.button('hB1',l='Locator Joints',c='handLoc()')
    hB2 = cmds.button('hB2',l='Create Rig',c='handCreation()') 
    ##call-------------Form
    cmds.formLayout(hand_form,e=True,af=[('hT1','top',5),('hT1','left',5),('hTF1','top',5),('hTF1','left',5),
                                    ('hT2','top',5),('hT2','left',5),('hTF2','top',5),('hTF2','left',5),('hS1','top',5),
                                    ('hB1','top',5),('hB1','right',5),('hB2','top',10),('hB2','right',5)],
                                    
                                    ac=[('hTF1','left',5,'hT1'),('hT2','top',10,'hT1'),('hTF2','top',10,'hTF1'),
                                    ('hTF2','left',10,'hT2'),('hS1','top',5,'hTF2'),('hB1','top',5,'hS1'),('hB2','top',5,'hB1')])
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.columnLayout('Hand',w=100,adj=True)
    cmds.button('cmbAll',l='Complete Rig',c='combRig()')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.showWindow(rigWin)
def armLoc():
    ##arm
    cmds.joint( p=(7, 155, 0), n='clavLocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(21, 152, -7), n='shoulderLocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(47, 152, -4), n='elbowLocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(77,152, 3), n='wristLocJoint' )
    cmds.select(clear=True)
    cmds.curve( name='clavCrv', d=1,p=[(7, 155, 0),(21, 152, -7)])
    cmds.curve( name='bicepCrv', d=1,p=[(21, 152, -7),(47, 152, -4)])
    cmds.curve( name='forearmCrv', d=1,p=[(47, 152, -4),(77,152, 3)])
    cmds.select(cl=True)
    cmds.skinCluster('clavLocJoint','shoulderLocJoint','clavCrv',tsb=True)
    cmds.skinCluster('shoulderLocJoint','elbowLocJoint','bicepCrv',tsb=True)
    cmds.skinCluster('elbowLocJoint','wristLocJoint','forearmCrv',tsb=True)
    cmds.select(cl=True)
def armCreation():
    armPref = cmds.textField('atf1',q=True,tx=True)
    armSuf= cmds.textField('atf2',q=True,tx=True)
    ##-----------------------------arm_rig part---------------------
    armJoint = ['clav','shoulder','elbow','wrist']
    armJointLoc = ['','','','']
    nArmJointLoc = ['','','','']
    for i in range(len(armJoint)):
        armJointLoc[i] = cmds.xform(armJoint[i]+'LocJoint',query=True,ws=True,t=True)
    for i in range(len(armJoint)):
        cmds.joint(n='L_'+armJoint[i]+'BndJoint',p=armJointLoc[i])
    for i in range(len(armJoint)):
        cmds.joint('L_'+armJoint[i]+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.select(cl=True)
    cmds.setAttr('L_'+armJoint[3]+'BndJoint.jointOrientX', 0)
    cmds.setAttr('L_'+armJoint[3]+'BndJoint.jointOrientY', 0)
    cmds.setAttr('L_'+armJoint[3]+'BndJoint.jointOrientZ', 0)
    for i in range(len(armJoint)):
        cmds.joint(n='L_'+armJoint[i]+'FK_joint',p=armJointLoc[i])
    for i in range(len(armJoint)):
        cmds.joint('L_'+armJoint[i]+'FK_joint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.select(cl=True)
    cmds.setAttr('L_'+armJoint[3]+'FK_joint.jointOrientX', 0)
    cmds.setAttr('L_'+armJoint[3]+'FK_joint.jointOrientY', 0)
    cmds.setAttr('L_'+armJoint[3]+'FK_joint.jointOrientZ', 0)
    cmds.setAttr('L_'+armJoint[0]+'FK_joint.visibility',0)
    for i in range(len(armJoint)):
        cmds.joint(n='L_'+armJoint[i]+'IK_joint',p=armJointLoc[i])
    for i in range(len(armJoint)):
        cmds.joint('L_'+armJoint[i]+'IK_joint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.select(cl=True)
    cmds.setAttr('L_'+armJoint[3]+'IK_joint.jointOrientX', 0)
    cmds.setAttr('L_'+armJoint[3]+'IK_joint.jointOrientY', 0)
    cmds.setAttr('L_'+armJoint[3]+'IK_joint.jointOrientZ', 0)
    cmds.setAttr('L_'+armJoint[0]+'IK_joint.visibility',0)
    cmds.delete('clavLocJoint','shoulderLocJoint','elbowLocJoint','wristLocJoint','clavCrv','bicepCrv','forearmCrv')
    cmds.select(cl=True)
    ## ------------------------------arm controls------------------
    for i in range(3):
        cmds.circle(n='L_'+armJoint[i+1]+'_FK_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=10.0,ch=False)
        cmds.group('L_'+armJoint[i+1]+'_FK_Ctrl',n='L_'+armJoint[i+1]+'_FK_CtrlGrp')
        cmds.parent('L_'+armJoint[i+1]+'_FK_CtrlGrp','L_'+armJoint[i+1]+'FK_joint',r=True)
        cmds.setAttr('L_'+armJoint[i+1]+'_FK_CtrlGrp.translateX', 0)
        cmds.setAttr('L_'+armJoint[i+1]+'_FK_CtrlGrp.translateY', 0)
        cmds.setAttr('L_'+armJoint[i+1]+'_FK_CtrlGrp.translateZ', 0)
        cmds.setAttr('L_'+armJoint[i+1]+'_FK_CtrlGrp.rotateZ', 90)
        cmds.parent('L_'+armJoint[i+1]+'_FK_CtrlGrp',w=True)
    ##----FKconstraint-----------
    for i in range(3):
        cmds.orientConstraint('L_'+armJoint[i+1]+'_FK_Ctrl','L_'+armJoint[i+1]+'FK_joint',mo=True)
        cmds.orientConstraint('L_'+armJoint[i+1]+'FK_joint','L_'+armJoint[i+1]+'BndJoint',mo=True)
    cmds.parent('L_'+armJoint[3]+'_FK_CtrlGrp','L_'+armJoint[2]+'_FK_Ctrl')
    cmds.parent('L_'+armJoint[2]+'_FK_CtrlGrp','L_'+armJoint[1]+'_FK_Ctrl')  
    ##ikCtrl--
    for i in range(3):
        cmds.circle(n='L_'+armJoint[i+1]+'_IK_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=6.0,ch=False)
        cmds.group('L_'+armJoint[i+1]+'_IK_Ctrl',n='L_'+armJoint[i+1]+'_IK_CtrlGrp')
        cmds.parent('L_'+armJoint[i+1]+'_IK_CtrlGrp','L_'+armJoint[i+1]+'IK_joint',r=True)
        cmds.setAttr('L_'+armJoint[i+1]+'_IK_CtrlGrp.translateX', 0)
        cmds.setAttr('L_'+armJoint[i+1]+'_IK_CtrlGrp.translateY', 0)
        cmds.setAttr('L_'+armJoint[i+1]+'_IK_CtrlGrp.translateZ', 0)
        cmds.setAttr('L_'+armJoint[i+1]+'_IK_CtrlGrp.rotateZ', 90)
        cmds.parent('L_'+armJoint[i+1]+'_IK_CtrlGrp',w=True) 
    cmds.setAttr('L_'+armJoint[2]+'_IK_CtrlGrp.rotateZ', 0)
    cmds.move(0,0,-15,'L_'+armJoint[2]+'_IK_CtrlGrp',r=True)
    cmds.scale(0.5,0.5,0.5,'L_'+armJoint[2]+'_IK_CtrlGrp',r=True)
    ##------------IK_Constraints--------
    for i in range(3):
        cmds.orientConstraint('L_'+armJoint[i+1]+'IK_joint','L_'+armJoint[i+1]+'BndJoint',mo=True)
    cmds.ikHandle(n='L_ArmIK',sj='L_'+armJoint[1]+'IK_joint',ee='L_'+armJoint[3]+'IK_joint',sol='ikRPsolver')    
    cmds.parent('L_ArmIK','L_'+armJoint[3]+'_IK_Ctrl')
    cmds.orientConstraint('L_'+armJoint[3]+'_IK_Ctrl','L_'+armJoint[3]+'IK_joint',mo=True)
    cmds.poleVectorConstraint('L_'+armJoint[2]+'_IK_Ctrl','L_ArmIK')
    ##------------FK_IK--Switch----------------------------
    cmds.curve(n='L_FK_IK_ctrl',d=1,p=[(-1,0,-1),(-1,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,1),
                                    (1,0,1),(1,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,-1),
                                    (-1,0,-1)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12])
    cmds.group('L_FK_IK_ctrl',n='L_FK_IK_ctrlGrp')
    cmds.parent('L_FK_IK_ctrlGrp','L_'+armJoint[3]+'BndJoint',r=True)
    cmds.setAttr("L_FK_IK_ctrlGrp.translateX", 0)
    cmds.setAttr("L_FK_IK_ctrlGrp.translateY", 0)
    cmds.setAttr("L_FK_IK_ctrlGrp.translateZ", 0)
    cmds.parent('L_FK_IK_ctrlGrp',w=True)
    cmds.move(0,8,0,'L_FK_IK_ctrlGrp',r=True)
    cmds.addAttr('L_FK_IK_ctrl',ln='L_FK_IK',at='long',min=0,max=1,dv=0)
    cmds.setAttr('L_FK_IK_ctrl.L_FK_IK',keyable=True)
    cmds.makeIdentity('L_FK_IK_ctrlGrp',apply=True)
    cmds.shadingNode('condition',asUtility=True,n='L_FK_IK_Condition')
    cmds.setAttr('L_FK_IK_Condition.colorIfTrueR',1)
    cmds.setAttr('L_FK_IK_Condition.colorIfTrueG',0)
    cmds.setAttr('L_FK_IK_Condition.colorIfFalseR',0)
    cmds.setAttr('L_FK_IK_Condition.colorIfFalseG',1)
    cmds.connectAttr('L_FK_IK_ctrl.L_FK_IK','L_FK_IK_Condition.firstTerm')
    cmds.connectAttr('L_FK_IK_Condition.outColorR','L_'+armJoint[3]+'BndJoint_orientConstraint1.'+'L_'+armJoint[3]+'FK_jointW0')
    cmds.connectAttr('L_FK_IK_Condition.outColorR','L_'+armJoint[2]+'BndJoint_orientConstraint1.'+'L_'+armJoint[2]+'FK_jointW0')
    cmds.connectAttr('L_FK_IK_Condition.outColorR','L_'+armJoint[1]+'BndJoint_orientConstraint1.'+'L_'+armJoint[1]+'FK_jointW0')
    cmds.connectAttr('L_FK_IK_Condition.outColorG','L_'+armJoint[3]+'BndJoint_orientConstraint1.'+'L_'+armJoint[3]+'IK_jointW1')
    cmds.connectAttr('L_FK_IK_Condition.outColorG','L_'+armJoint[2]+'BndJoint_orientConstraint1.'+'L_'+armJoint[2]+'IK_jointW1')
    cmds.connectAttr('L_FK_IK_Condition.outColorG','L_'+armJoint[1]+'BndJoint_orientConstraint1.'+'L_'+armJoint[1]+'IK_jointW1')
    cmds.connectAttr('L_FK_IK_Condition.outColorR','L_'+armJoint[1]+'_FK_CtrlGrp.visibility')
    cmds.connectAttr('L_FK_IK_Condition.outColorG','L_'+armJoint[3]+'_IK_CtrlGrp.visibility')
    cmds.connectAttr('L_FK_IK_Condition.outColorG','L_'+armJoint[2]+'_IK_CtrlGrp.visibility')
    ##-----------------negative Side-------------------
    for i in range(len(armJointLoc)):
        negX = armJointLoc[i]
        negVal = negX[0]*-1
        negX[0]= negVal
        nArmJointLoc[i] = negX

    for i in range(len(armJoint)):
        cmds.joint(n='R_'+armJoint[i]+'BndJoint',p=nArmJointLoc[i])
    for i in range(len(armJoint)):
        cmds.joint('R_'+armJoint[i]+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.select(cl=True)
    cmds.setAttr('R_'+armJoint[3]+'BndJoint.jointOrientX', 0)
    cmds.setAttr('R_'+armJoint[3]+'BndJoint.jointOrientY', 0)
    cmds.setAttr('R_'+armJoint[3]+'BndJoint.jointOrientZ', 0)

    for i in range(len(armJoint)):
        cmds.joint(n='R_'+armJoint[i]+'FK_joint',p=nArmJointLoc[i])
    for i in range(len(armJoint)):
        cmds.joint('R_'+armJoint[i]+'FK_joint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.select(cl=True)
    cmds.setAttr('R_'+armJoint[3]+'FK_joint.jointOrientX', 0)
    cmds.setAttr('R_'+armJoint[3]+'FK_joint.jointOrientY', 0)
    cmds.setAttr('R_'+armJoint[3]+'FK_joint.jointOrientZ', 0)
    cmds.setAttr('R_'+armJoint[0]+'FK_joint.visibility',0)
    for i in range(len(armJoint)):
        cmds.joint(n='R_'+armJoint[i]+'IK_joint',p=nArmJointLoc[i])
    for i in range(len(armJoint)):
        cmds.joint('R_'+armJoint[i]+'IK_joint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.select(cl=True)
    cmds.setAttr('R_'+armJoint[3]+'IK_joint.jointOrientX', 0)
    cmds.setAttr('R_'+armJoint[3]+'IK_joint.jointOrientY', 0)
    cmds.setAttr('R_'+armJoint[3]+'IK_joint.jointOrientZ', 0)
    cmds.setAttr('R_'+armJoint[0]+'IK_joint.visibility',0)
    cmds.select(cl=True)
    ## ------------------------------arm controls------------------
    for i in range(3):
        cmds.circle(n='R_'+armJoint[i+1]+'_FK_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=10.0,ch=False)
        cmds.group('R_'+armJoint[i+1]+'_FK_Ctrl',n='R_'+armJoint[i+1]+'_FK_CtrlGrp')
        cmds.parent('R_'+armJoint[i+1]+'_FK_CtrlGrp','R_'+armJoint[i+1]+'FK_joint',r=True)
        cmds.setAttr('R_'+armJoint[i+1]+'_FK_CtrlGrp.translateX', 0)
        cmds.setAttr('R_'+armJoint[i+1]+'_FK_CtrlGrp.translateY', 0)
        cmds.setAttr('R_'+armJoint[i+1]+'_FK_CtrlGrp.translateZ', 0)
        cmds.setAttr('R_'+armJoint[i+1]+'_FK_CtrlGrp.rotateZ', 90)
        cmds.parent('R_'+armJoint[i+1]+'_FK_CtrlGrp',w=True)
    ##----FKconstraint-----------
    for i in range(3):
        cmds.orientConstraint('R_'+armJoint[i+1]+'_FK_Ctrl','R_'+armJoint[i+1]+'FK_joint',mo=True)
        cmds.orientConstraint('R_'+armJoint[i+1]+'FK_joint','R_'+armJoint[i+1]+'BndJoint',mo=True)
    cmds.parent('R_'+armJoint[3]+'_FK_CtrlGrp','R_'+armJoint[2]+'_FK_Ctrl')
    cmds.parent('R_'+armJoint[2]+'_FK_CtrlGrp','R_'+armJoint[1]+'_FK_Ctrl')  
    ##ikCtrl--
    for i in range(3):
        cmds.circle(n='R_'+armJoint[i+1]+'_IK_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=6.0,ch=False)
        cmds.group('R_'+armJoint[i+1]+'_IK_Ctrl',n='R_'+armJoint[i+1]+'_IK_CtrlGrp')
        cmds.parent('R_'+armJoint[i+1]+'_IK_CtrlGrp','R_'+armJoint[i+1]+'IK_joint',r=True)
        cmds.setAttr('R_'+armJoint[i+1]+'_IK_CtrlGrp.translateX', 0)
        cmds.setAttr('R_'+armJoint[i+1]+'_IK_CtrlGrp.translateY', 0)
        cmds.setAttr('R_'+armJoint[i+1]+'_IK_CtrlGrp.translateZ', 0)
        cmds.setAttr('R_'+armJoint[i+1]+'_IK_CtrlGrp.rotateZ', 90)
        cmds.parent('R_'+armJoint[i+1]+'_IK_CtrlGrp',w=True) 
    cmds.setAttr('R_'+armJoint[2]+'_IK_CtrlGrp.rotateZ', 0)
    cmds.move(0,0,-15,'R_'+armJoint[2]+'_IK_CtrlGrp',r=True)
    cmds.scale(0.5,0.5,0.5,'R_'+armJoint[2]+'_IK_CtrlGrp',r=True)
    ##------------IK_Constraints--------
    for i in range(3):
        cmds.orientConstraint('R_'+armJoint[i+1]+'IK_joint','R_'+armJoint[i+1]+'BndJoint',mo=True)
    cmds.ikHandle(n='R_ArmIK',sj='R_'+armJoint[1]+'IK_joint',ee='R_'+armJoint[3]+'IK_joint',sol='ikRPsolver')    
    cmds.parent('R_ArmIK','R_'+armJoint[3]+'_IK_Ctrl')
    cmds.orientConstraint('R_'+armJoint[3]+'_IK_Ctrl','R_'+armJoint[3]+'IK_joint',mo=True)
    cmds.poleVectorConstraint('R_'+armJoint[2]+'_IK_Ctrl','R_ArmIK')
    ##------------FK_IK--Switch----------------------------
    cmds.curve(n='R_FK_IK_ctrl',d=1,p=[(-1,0,-1),(-1,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,1),
                                    (1,0,1),(1,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,-1),
                                    (-1,0,-1)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12])
    cmds.group('R_FK_IK_ctrl',n='R_FK_IK_ctrlGrp')
    cmds.parent('R_FK_IK_ctrlGrp','R_'+armJoint[3]+'BndJoint',r=True)
    cmds.setAttr("R_FK_IK_ctrlGrp.translateX", 0)
    cmds.setAttr("R_FK_IK_ctrlGrp.translateY", 0)
    cmds.setAttr("R_FK_IK_ctrlGrp.translateZ", 0)
    cmds.parent('R_FK_IK_ctrlGrp',w=True)
    cmds.move(0,8,0,'R_FK_IK_ctrlGrp',r=True)
    cmds.addAttr('R_FK_IK_ctrl',ln='R_FK_IK',at='long',min=0,max=1,dv=0)
    cmds.setAttr('R_FK_IK_ctrl.R_FK_IK',keyable=True)
    cmds.makeIdentity('R_FK_IK_ctrlGrp',apply=True)
    cmds.shadingNode('condition',asUtility=True,n='R_FK_IK_Condition')
    cmds.setAttr('R_FK_IK_Condition.colorIfTrueR',1)
    cmds.setAttr('R_FK_IK_Condition.colorIfTrueG',0)
    cmds.setAttr('R_FK_IK_Condition.colorIfFalseR',0)
    cmds.setAttr('R_FK_IK_Condition.colorIfFalseG',1)
    cmds.connectAttr('R_FK_IK_ctrl.R_FK_IK','R_FK_IK_Condition.firstTerm')
    cmds.connectAttr('R_FK_IK_Condition.outColorR','R_'+armJoint[3]+'BndJoint_orientConstraint1.'+'R_'+armJoint[3]+'FK_jointW0')
    cmds.connectAttr('R_FK_IK_Condition.outColorR','R_'+armJoint[2]+'BndJoint_orientConstraint1.'+'R_'+armJoint[2]+'FK_jointW0')
    cmds.connectAttr('R_FK_IK_Condition.outColorR','R_'+armJoint[1]+'BndJoint_orientConstraint1.'+'R_'+armJoint[1]+'FK_jointW0')
    cmds.connectAttr('R_FK_IK_Condition.outColorG','R_'+armJoint[3]+'BndJoint_orientConstraint1.'+'R_'+armJoint[3]+'IK_jointW1')
    cmds.connectAttr('R_FK_IK_Condition.outColorG','R_'+armJoint[2]+'BndJoint_orientConstraint1.'+'R_'+armJoint[2]+'IK_jointW1')
    cmds.connectAttr('R_FK_IK_Condition.outColorG','R_'+armJoint[1]+'BndJoint_orientConstraint1.'+'R_'+armJoint[1]+'IK_jointW1')
    cmds.connectAttr('R_FK_IK_Condition.outColorR','R_'+armJoint[1]+'_FK_CtrlGrp.visibility')
    cmds.connectAttr('R_FK_IK_Condition.outColorG','R_'+armJoint[3]+'_IK_CtrlGrp.visibility')
    cmds.connectAttr('R_FK_IK_Condition.outColorG','R_'+armJoint[2]+'_IK_CtrlGrp.visibility')
def legLoc():
    
    ##Leg joint place
    cmds.joint( p=(10.257, 92.943, -1.846), n='hipLocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(10.257, 46.375, -1.613), n='kneeLocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(10.257, 9.492, -9.297), n='ankleLocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(10.257, 0, -0.108), n='ballLocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(10.257, 0, 11.317), n='toeLocJoint' )
    cmds.select(clear=True)
    cmds.curve( name='thighCrv', d=1,p=[(10.257, 92.943, -1.846),(10.257, 46.375, -1.613)])
    cmds.curve( name='shinCrv', d=1,p=[(10.257, 46.375, -1.613),(10.257, 9.492, -9.297)])
    cmds.curve( name='archCrv', d=1,p=[(10.257, 9.492, -9.297),(10.257, 0, -0.108)])
    cmds.curve( name='toeCrv', d=1,p=[(10.257, 0, -0.108),(10.257, 0, 11.317)])
    cmds.select(clear=True)
    cmds.skinCluster('hipLocJoint','kneeLocJoint','thighCrv',tsb=True)
    cmds.skinCluster('ankleLocJoint','kneeLocJoint','shinCrv',tsb=True)
    cmds.skinCluster('ankleLocJoint','ballLocJoint','archCrv',tsb=True)
    cmds.skinCluster('toeLocJoint','ballLocJoint','toeCrv',tsb=True)
    cmds.select(cl=True)
def legCreation():
    legPref = cmds.textField('ltf1',q=True,tx=True)
    legSuf= cmds.textField('ltf2',q=True,tx=True)
    ##-----leg
    legJoint = ['hip','knee','ankle','ball','toe']
    legJointLoc= ['','','','','']
    nLegJointLoc=['','','','','']
    footCtrls = ['Ankle_Twist','Heel_Lift','Toe_Lift','Ball_Rotate','Toe_Tap']

    ##----joint setup
    for i in range(5):
        legJointLoc[i] = cmds.xform(legJoint[i]+'LocJoint',query=True,ws=True,t=True)
    for i in range(5):
        cmds.joint(n='L_'+legJoint[i]+'ctrlJoint',p=legJointLoc[i])
    for i in range(5):
        cmds.joint('L_'+legJoint[i]+'ctrlJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    ballPlace= legJointLoc[3]
    anklePlace= legJointLoc[2]
    toePlace = legJointLoc[4]
    cmds.setAttr('L_toectrlJoint.jointOrientX', 0)
    cmds.setAttr('L_toectrlJoint.jointOrientY', 0)
    cmds.setAttr('L_toectrlJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    for i in range(5):
        cmds.joint(n='L_'+legJoint[i]+'BndJoint',p=legJointLoc[i])
    for i in range(5):
        cmds.joint('L_'+legJoint[i]+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('L_toeBndJoint.jointOrientX', 0)
    cmds.setAttr('L_toeBndJoint.jointOrientY', 0)
    cmds.setAttr('L_toeBndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    print legJointLoc
    cmds.curve(n='L_Foot_Ctrl',d=1,p=[(-5,0,15),(5,0,15),(5,0,-15),(-5,0,-15),(-5,0,15)],k=[0,1,2,3,4])
    for i in range(len(footCtrls)):
        cmds.addAttr('L_Foot_Ctrl',ln=footCtrls[i],dv=0)
        cmds.setAttr('L_Foot_Ctrl.'+footCtrls[i],e=True,keyable=True)
    cmds.select(cl=True)
    for i in range(len(footCtrls)):
        cmds.group(n='L_'+footCtrls[i]+'_Null',em=True)
    cmds.parent('L_'+footCtrls[4]+'_Null','L_'+footCtrls[3]+'_Null','L_'+footCtrls[2]+'_Null')
    cmds.parent('L_'+footCtrls[2]+'_Null','L_'+footCtrls[1]+'_Null')
    cmds.parent('L_'+footCtrls[1]+'_Null','L_'+footCtrls[0]+'_Null')
    cmds.parent('L_'+footCtrls[0]+'_Null','L_Foot_Ctrl')
    cmds.move(ballPlace[0],0,ballPlace[2],'L_Foot_Ctrl',r=True)
    cmds.makeIdentity('L_Foot_Ctrl',apply=True,translate=True)
    cmds.move(anklePlace[0],anklePlace[1],anklePlace[2],'L_'+footCtrls[0]+'_Null',ws=True,rpr=True,spr=True)
    cmds.move(toePlace[0],toePlace[1],toePlace[2],'L_'+footCtrls[2]+'_Null',ws=True,rpr=True,spr=True)
    cmds.move(ballPlace[0],ballPlace[1],ballPlace[2],'L_'+footCtrls[3]+'_Null',ws=True,rpr=True,spr=True)
    cmds.move(ballPlace[0],ballPlace[1],ballPlace[2],'L_'+footCtrls[4]+'_Null',ws=True,rpr=True,spr=True)
    for i in range(len(footCtrls)):
        cmds.makeIdentity('L_'+footCtrls[i]+'_Null',apply=True,translate=True)
    ##--IK--Handles------------------
    cmds.ikHandle(n='L_AnkleIK',sj='L_'+legJoint[0]+'ctrlJoint',ee='L_'+legJoint[2]+'ctrlJoint',sol='ikRPsolver')
    cmds.ikHandle(n='L_BallIK',sj='L_'+legJoint[2]+'ctrlJoint',ee='L_'+legJoint[3]+'ctrlJoint',sol='ikRPsolver')
    cmds.ikHandle(n='L_ToeIK',sj='L_'+legJoint[3]+'ctrlJoint',ee='L_'+legJoint[4]+'ctrlJoint',sol='ikRPsolver')
    cmds.parent('L_AnkleIK','L_'+footCtrls[3]+'_Null')
    cmds.parent('L_BallIK','L_ToeIK','L_'+footCtrls[4]+'_Null')
    cmds.connectAttr('L_Foot_Ctrl.'+footCtrls[0],'L_'+footCtrls[0]+'_Null.rotateY')
    cmds.connectAttr('L_Foot_Ctrl.'+footCtrls[1],'L_'+footCtrls[1]+'_Null.rotateX')
    cmds.connectAttr('L_Foot_Ctrl.'+footCtrls[2],'L_'+footCtrls[2]+'_Null.rotateX')
    cmds.connectAttr('L_Foot_Ctrl.'+footCtrls[3],'L_'+footCtrls[3]+'_Null.rotateX')
    cmds.connectAttr('L_Foot_Ctrl.'+footCtrls[4],'L_'+footCtrls[4]+'_Null.rotateX')
    ##----------------------------------kneeCtrl------
    cmds.circle(n='L_Knee_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=2.0,ch=False)
    cmds.group('L_Knee_Ctrl',n='L_Knee_CtrlGrp')
    cmds.parent('L_Knee_CtrlGrp','L_'+legJoint[1]+'ctrlJoint',r=True)
    cmds.setAttr("L_Knee_CtrlGrp.translateX", 0)
    cmds.setAttr("L_Knee_CtrlGrp.translateY", -15)
    cmds.setAttr("L_Knee_CtrlGrp.translateZ", 0)
    cmds.setAttr('L_Knee_CtrlGrp.rotateZ', 90)
    cmds.parent('L_Knee_CtrlGrp',w=True)
    cmds.poleVectorConstraint('L_Knee_Ctrl','L_AnkleIK')
    for i in range(len(legJoint)):
        cmds.parentConstraint('L_'+legJoint[i]+'ctrlJoint','L_'+legJoint[i]+'BndJoint',mo=True)
    for i in range(len(legJointLoc)):
        negX = legJointLoc[i]
        negVal = negX[0]*-1
        negX[0]= negVal
        nLegJointLoc[i] = negX
    cmds.select(cl=True)
    cmds.delete('hipLocJoint','thighCrv','kneeLocJoint','shinCrv','ankleLocJoint','ballLocJoint','archCrv','toeLocJoint','toeCrv')
    for i in range(5):
        cmds.joint(n='R_'+legJoint[i]+'ctrlJoint',p=legJointLoc[i])
    for i in range(5):
        cmds.joint('R_'+legJoint[i]+'ctrlJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    ballPlace= legJointLoc[3]
    anklePlace= legJointLoc[2]
    toePlace = legJointLoc[4]
    cmds.setAttr('R_toectrlJoint.jointOrientX', 0)
    cmds.setAttr('R_toectrlJoint.jointOrientY', 0)
    cmds.setAttr('R_toectrlJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    for i in range(5):
        cmds.joint(n='R_'+legJoint[i]+'BndJoint',p=legJointLoc[i])
    for i in range(5):
        cmds.joint('R_'+legJoint[i]+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('R_toeBndJoint.jointOrientX', 0)
    cmds.setAttr('R_toeBndJoint.jointOrientY', 0)
    cmds.setAttr('R_toeBndJoint.jointOrientZ', 0)
    cmds.select(cl=True)

    cmds.curve(n='R_Foot_Ctrl',d=1,p=[(-5,0,15),(5,0,15),(5,0,-15),(-5,0,-15),(-5,0,15)],k=[0,1,2,3,4])
    for i in range(len(footCtrls)):
        cmds.addAttr('R_Foot_Ctrl',ln=footCtrls[i],dv=0)
        cmds.setAttr('R_Foot_Ctrl.'+footCtrls[i],e=True,keyable=True)
    cmds.select(cl=True)
    for i in range(len(footCtrls)):
        cmds.group(n='R_'+footCtrls[i]+'_Null',em=True)
    cmds.parent('R_'+footCtrls[4]+'_Null','R_'+footCtrls[3]+'_Null','R_'+footCtrls[2]+'_Null')
    cmds.parent('R_'+footCtrls[2]+'_Null','R_'+footCtrls[1]+'_Null')
    cmds.parent('R_'+footCtrls[1]+'_Null','R_'+footCtrls[0]+'_Null')
    cmds.parent('R_'+footCtrls[0]+'_Null','R_Foot_Ctrl')
    cmds.move(ballPlace[0],0,ballPlace[2],'R_Foot_Ctrl',r=True)
    cmds.makeIdentity('R_Foot_Ctrl',apply=True,translate=True)
    cmds.move(anklePlace[0],anklePlace[1],anklePlace[2],'R_'+footCtrls[0]+'_Null',ws=True,rpr=True,spr=True)
    cmds.move(toePlace[0],toePlace[1],toePlace[2],'R_'+footCtrls[2]+'_Null',ws=True,rpr=True,spr=True)
    cmds.move(ballPlace[0],ballPlace[1],ballPlace[2],'R_'+footCtrls[3]+'_Null',ws=True,rpr=True,spr=True)
    cmds.move(ballPlace[0],ballPlace[1],ballPlace[2],'R_'+footCtrls[4]+'_Null',ws=True,rpr=True,spr=True)
    for i in range(len(footCtrls)):
        cmds.makeIdentity('R_'+footCtrls[i]+'_Null',apply=True,translate=True)
    ##--IK--Handles------------------
    cmds.ikHandle(n='R_AnkleIK',sj='R_'+legJoint[0]+'ctrlJoint',ee='R_'+legJoint[2]+'ctrlJoint',sol='ikRPsolver')
    cmds.ikHandle(n='R_BallIK',sj='R_'+legJoint[2]+'ctrlJoint',ee='R_'+legJoint[3]+'ctrlJoint',sol='ikRPsolver')
    cmds.ikHandle(n='R_ToeIK',sj='R_'+legJoint[3]+'ctrlJoint',ee='R_'+legJoint[4]+'ctrlJoint',sol='ikRPsolver')
    cmds.parent('R_AnkleIK','R_'+footCtrls[3]+'_Null')
    cmds.parent('R_BallIK','R_ToeIK','R_'+footCtrls[4]+'_Null')
    cmds.connectAttr('R_Foot_Ctrl.'+footCtrls[0],'R_'+footCtrls[0]+'_Null.rotateY')
    cmds.connectAttr('R_Foot_Ctrl.'+footCtrls[1],'R_'+footCtrls[1]+'_Null.rotateX')
    cmds.connectAttr('R_Foot_Ctrl.'+footCtrls[2],'R_'+footCtrls[2]+'_Null.rotateX')
    cmds.connectAttr('R_Foot_Ctrl.'+footCtrls[3],'R_'+footCtrls[3]+'_Null.rotateX')
    cmds.connectAttr('R_Foot_Ctrl.'+footCtrls[4],'R_'+footCtrls[4]+'_Null.rotateX')
    ##----------------------------------kneeCtrl------
    cmds.circle(n='R_Knee_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=2.0,ch=False)
    cmds.group('R_Knee_Ctrl',n='R_Knee_CtrlGrp')
    cmds.parent('R_Knee_CtrlGrp','R_'+legJoint[1]+'ctrlJoint',r=True)
    cmds.setAttr("R_Knee_CtrlGrp.translateX", 0)
    cmds.setAttr("R_Knee_CtrlGrp.translateY", -15)
    cmds.setAttr("R_Knee_CtrlGrp.translateZ", 0)
    cmds.setAttr('R_Knee_CtrlGrp.rotateZ', 90)
    cmds.parent('R_Knee_CtrlGrp',w=True)
    cmds.poleVectorConstraint('R_Knee_Ctrl','R_AnkleIK')
    for i in range(len(legJoint)):
        cmds.parentConstraint('R_'+legJoint[i]+'ctrlJoint','R_'+legJoint[i]+'BndJoint',mo=True)
def spineLoc():
   
##------------------spineLoc------Joints--------------------------------------
    cmds.joint( p=(0, 93, -5), n='lowSpineLocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(0, 157, -10), n='highSpineLocJoint' )
    cmds.select(clear=True)
    cmds.curve( name='spinePlCrv', d=1,p=[(0, 93, -5),(0, 157, -10)])
    cmds.select(clear=True)
    cmds.skinCluster('lowSpineLocJoint','highSpineLocJoint','spinePlCrv',tsb=True)
    cmds.select(cl=True)
    ##---------Neck_loc--------------------------
    cmds.joint( p=(0, 157, -10), n='bNeckLocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(0,168,-6), n='tNeckLocJoint' )
    cmds.select(cl=True)
    cmds.joint( p=(0,190,-4), n='headLocJoint' )
    cmds.select(cl=True)
    cmds.curve( name='neckPlCrv', d=1,p=[(0, 157, -10),(0,168,-6)])
    cmds.curve( name='headPlCrv', d=1,p=[(0,168,-6),(0,190,-4)])
    cmds.select(cl=True)
    cmds.skinCluster('tNeckLocJoint','bNeckLocJoint','neckPlCrv',tsb=True)
    cmds.skinCluster('tNeckLocJoint','headLocJoint','headPlCrv',tsb=True)
    cmds.select(cl=True)
def spineCreation():
    spinePref = cmds.textField('sPFtf1',q=True,tx=True)
    spineSuf = cmds.textField('sSFtf1',q=True,tx=True)
    ##------------------Advanced--IK--Spine----------------------------
    backJoint=['Spine_01','Spine_02','Spine_03','Spine_04','Spine_05']
    backJointLoc = ['','','','','','']
    backJointLoc[0] = cmds.xform('lowSpineLocJoint',query=True,ws=True,t=True)
    backJointLoc[4] = cmds.xform('highSpineLocJoint',query=True,ws=True,t=True)
    cmds.duplicate('spinePlCrv', n='spineCtrlCrv')
    cmds.rebuildCurve('spineCtrlCrv',rt=0,s=4)
    cmds.arclen('spineCtrlCrv', ch=True)
    cmds.rename('curveInfo1','spineCrvInfo')
    curSpLen = cmds.getAttr('spineCrvInfo.arcLength')
    stepLen= curSpLen/4
    cmds.joint(n=backJoint[0]+'_BndJoint',p=backJointLoc[0])
    cmds.joint(n=backJoint[1]+'_BndJoint',p=backJointLoc[4])
    cmds.joint(backJoint[0]+'_BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr(backJoint[1]+'_BndJoint.jointOrientX', 0 )
    cmds.setAttr(backJoint[1]+'_BndJoint.jointOrientY', 0 )
    cmds.setAttr(backJoint[1]+'_BndJoint.jointOrientZ', 0 )
    cmds.select(clear=True)
    cmds.delete('lowSpineLocJoint','highSpineLocJoint','spinePlCrv')
    ##-------------------bnd_joints
    for i in range(3):
        cmds.insertJoint(backJoint[i+1]+'_BndJoint')
        cmds.rename(backJoint[i+2]+'_BndJoint')
    for i in range(4):
        cmds.joint(backJoint[i+1]+'_BndJoint',e=True,r=True,p=(stepLen,0,0))
    for i in range(len(backJoint)):
        backJointLoc[i]= cmds.xform(backJoint[i]+'_BndJoint',query=True,ws=True,t=True)
    cmds.select(cl=True)
    ##--------Ctrl_Joints-------------------
    cmds.joint(n=backJoint[0]+'_ctrlJoint',p=backJointLoc[0])
    cmds.joint(n=backJoint[1]+'_ctrlJoint',p=backJointLoc[4])
    cmds.joint(backJoint[0]+'_ctrlJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr(backJoint[1]+'_ctrlJoint.jointOrientX', 0 )
    cmds.setAttr(backJoint[1]+'_ctrlJoint.jointOrientY', 0 )
    cmds.setAttr(backJoint[1]+'_ctrlJoint.jointOrientZ', 0 )
    cmds.select(cl=True)
    for i in range(3):
        cmds.insertJoint(backJoint[i+1]+'_ctrlJoint')
        cmds.rename(backJoint[i+2]+'_ctrlJoint')
    for i in range(4):
        cmds.joint(backJoint[i+1]+'_ctrlJoint',e=True,r=True,p=(stepLen,0,0))
    for i in range(len(backJoint)):
        backJointLoc[i]= cmds.xform(backJoint[i]+'_ctrlJoint',query=True,ws=True,t=True)
    cmds.select(cl=True)
    cmds.joint(n='low_Ctrl_Joint',p=backJointLoc[0],rad=2)
    cmds.select(cl=True)
    cmds.joint(n='mid_Ctrl_Joint',p=backJointLoc[2],rad=2)
    cmds.select(cl=True)
    cmds.joint(n='top_Ctrl_Joint',p=backJointLoc[4],rad=2)
    cmds.select(cl=True)
    cmds.ikHandle(n='spineIK',sol='ikSplineSolver',sj=backJoint[0]+'_ctrlJoint',ee=backJoint[4]+'_ctrlJoint',fj=True,c='spineCtrlCrv')
    cmds.skinCluster('low_Ctrl_Joint','mid_Ctrl_Joint','top_Ctrl_Joint','spineCtrlCrv',tsb=True)
    ##---------Spine---Ctrls--------------------------------
    cmds.circle(n='top_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=15.0,ch=False)
    cmds.group('top_Ctrl',n='top_CtrlGrp')
    cmds.circle(n='mid_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=15.0,ch=False)
    cmds.group('mid_Ctrl',n='mid_CtrlGrp')
    cmds.circle(n='low_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=15.0,ch=False)
    cmds.group('low_Ctrl',n='low_CtrlGrp')
    cmds.circle(n='hip_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=17.0,ch=False)
    cmds.parent('top_CtrlGrp','Spine_05_ctrlJoint',r=True)
    cmds.setAttr("top_CtrlGrp.translateX", 0)
    cmds.setAttr("top_CtrlGrp.translateY", 0)
    cmds.setAttr("top_CtrlGrp.translateZ", 0)
    cmds.setAttr("top_CtrlGrp.rotateZ", 90)
    cmds.parent('mid_CtrlGrp','Spine_03_ctrlJoint',r=True)
    cmds.setAttr("mid_CtrlGrp.translateX", 0)
    cmds.setAttr("mid_CtrlGrp.translateY", 0)
    cmds.setAttr("mid_CtrlGrp.translateZ", 0)
    cmds.setAttr("mid_CtrlGrp.rotateZ", 90)
    cmds.parent('low_CtrlGrp','Spine_01_ctrlJoint',r=True)
    cmds.setAttr("low_CtrlGrp.translateX", 0)
    cmds.setAttr("low_CtrlGrp.translateY", 0)
    cmds.setAttr("low_CtrlGrp.translateZ", 0)
    cmds.setAttr("low_CtrlGrp.rotateZ", 90)
    cmds.parent('hip_Ctrl','Spine_01_ctrlJoint',r=True)
    cmds.setAttr("hip_Ctrl.translateX", 0)
    cmds.setAttr("hip_Ctrl.translateY", 0)
    cmds.setAttr("hip_Ctrl.translateZ", 0)
    cmds.setAttr("hip_Ctrl.rotateZ", 90)
    cmds.parent('top_CtrlGrp',w=True)
    cmds.parent('mid_CtrlGrp',w=True)
    cmds.parent('low_CtrlGrp',w=True)
    cmds.parent('hip_Ctrl',w=True)
    cmds.parent('low_Ctrl_Joint','low_Ctrl')
    cmds.parent('mid_Ctrl_Joint','mid_Ctrl')
    cmds.parent('top_Ctrl_Joint','top_Ctrl')
    cmds.parent('low_CtrlGrp','mid_CtrlGrp','top_CtrlGrp','hip_Ctrl')
    cmds.parentConstraint('top_Ctrl','mid_CtrlGrp',mo=True)
    ##--------advanced_Twist
    cmds.setAttr('spineIK.dTwistControlEnable', 1)
    cmds.setAttr('spineIK.dWorldUpType', 4)
    cmds.setAttr('spineIK.dWorldUpAxis', 1)
    cmds.setAttr("spineIK.dWorldUpVectorZ", 1)
    cmds.setAttr("spineIK.dWorldUpVectorY", 0)
    cmds.setAttr("spineIK.dWorldUpVectorEndY", 0)
    cmds.setAttr("spineIK.dWorldUpVectorEndZ" ,1)
    cmds.connectAttr('low_Ctrl.xformMatrix',"spineIK.dWorldUpMatrix")
    cmds.connectAttr('top_Ctrl.xformMatrix',"spineIK.dWorldUpMatrixEnd")
    ##-------------Squash----Stretch-------------------
    cmds.shadingNode('multiplyDivide',asUtility=True,n='crvLenMulDiv')
    cmds.shadingNode('condition',asUtility=True,n='crvCondition')
    cmds.setAttr('crvLenMulDiv.operation', 2)
    cmds.setAttr('crvLenMulDiv.input2X', curSpLen)
    cmds.setAttr('crvCondition.secondTerm',1)
    cmds.setAttr('crvCondition.colorIfTrueR',1)
    cmds.setAttr('crvCondition.colorIfFalseG',0)
    cmds.setAttr('crvCondition.colorIfFalseB',0)
    cmds.connectAttr('spineCrvInfo.arcLength','crvLenMulDiv.input1X')
    cmds.connectAttr('crvLenMulDiv.outputX','crvCondition.firstTerm')
    cmds.connectAttr('crvLenMulDiv.outputX','crvCondition.colorIfFalseR')
    for i in range(4):
        cmds.connectAttr('crvCondition.outColorR',backJoint[i]+'_ctrlJoint.scaleX')
    for i in range(5):
        cmds.parentConstraint(backJoint[i]+'_ctrlJoint',backJoint[i]+'_BndJoint',mo=True)
    ##----Neck_Stuff-------
    neckJoint=['bNeck','tNeck','head']
    neckJointLoc=['','','']
    for i in range(len(neckJoint)):
        neckJointLoc[i] = cmds.xform(neckJoint[i]+'LocJoint',query=True,ws=True,t=True)
    for i in range(len(neckJoint)):
        cmds.joint(n=neckJoint[i]+'BndJoint',p=neckJointLoc[i])
    for i in range(len(neckJoint)):
        cmds.joint(neckJoint[i]+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.select(cl=True)
    for i in range(len(neckJoint)):
        neckJointLoc[i] = cmds.xform(neckJoint[i]+'LocJoint',query=True,ws=True,t=True)
    for i in range(len(neckJoint)):
        cmds.joint(n=neckJoint[i]+'ctrlJoint',p=neckJointLoc[i])
    for i in range(len(neckJoint)):
        cmds.joint(neckJoint[i]+'ctrlJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.select(cl=True)
    cmds.delete('neckPlCrv','headPlCrv','bNeckLocJoint','tNeckLocJoint','headLocJoint')
    ##------------------Neck--Ctrls--------------------------------
    cmds.curve(n=neckJoint[0]+'_Ctrl',d=1 ,p=[(0,0,0),(0,0,-9),(0,4,-13),(0,0,-17),(0,-4,-13),(0,0,-9)],k=[0,1,2,3,4,5])
    cmds.group(neckJoint[0]+'_Ctrl',n=neckJoint[0]+'_CtrlGrp')
    cmds.parent(neckJoint[0]+'_CtrlGrp',neckJoint[0]+'BndJoint')
    cmds.setAttr(neckJoint[0]+'_CtrlGrp.translateX',0)
    cmds.setAttr(neckJoint[0]+'_CtrlGrp.translateY',0)
    cmds.setAttr(neckJoint[0]+'_CtrlGrp.translateZ',0)
    cmds.parent(neckJoint[0]+'_CtrlGrp',w=True)
    cmds.curve(n=neckJoint[1]+'_Ctrl',d=1 ,p=[(0,0,0),(0,0,-9),(0,4,-13),(0,0,-17),(0,-4,-13),(0,0,-9)],k=[0,1,2,3,4,5])
    cmds.group(neckJoint[1]+'_Ctrl',n=neckJoint[1]+'_CtrlGrp')
    cmds.parent(neckJoint[1]+'_CtrlGrp',neckJoint[1]+'BndJoint')
    cmds.setAttr(neckJoint[1]+'_CtrlGrp.translateX',0)
    cmds.setAttr(neckJoint[1]+'_CtrlGrp.translateY',0)
    cmds.setAttr(neckJoint[1]+'_CtrlGrp.translateZ',0)
    cmds.parent(neckJoint[1]+'_CtrlGrp',w=True)
    ##---------------Neck---setup----------------------
    cmds.parent(neckJoint[0]+'_Ctrl',neckJoint[1]+'_CtrlGrp')
    cmds.orientConstraint(neckJoint[0]+'_Ctrl',neckJoint[0]+'ctrlJoint',mo=True)
    cmds.orientConstraint(neckJoint[1]+'_Ctrl',neckJoint[1]+'ctrlJoint',mo=True)
    cmds.group(em=True,n='topSpine_Null')
    cmds.parent('topSpine_Null',backJoint[4]+'_ctrlJoint')
    cmds.setAttr('topSpine_Null.translateX',0)
    cmds.setAttr('topSpine_Null.translateY',0)
    cmds.setAttr('topSpine_Null.translateZ',0)
    cmds.parent(neckJoint[0]+'ctrlJoint','topSpine_Null')
    cmds.parent(neckJoint[1]+'_CtrlGrp','topSpine_Null')
    for i in range(len(neckJoint)):
        cmds.parentConstraint(neckJoint[i]+'ctrlJoint',neckJoint[i]+'BndJoint',mo=True)
def handLoc():
    
    cmds.joint( p=(83, 152, 3), n='handLocJoint' )
    cmds.select(clear=True)
    #Thumb
    cmds.joint( p=(80,152,8), n='thumb1LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(83,152,12), n='thumb2LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(85, 151, 15), n='thumb3LocJoint' )
    cmds.select(clear=True)
    cmds.curve( name='thumb1Crv', d=1,p=[(80,152,8),(83,152,12)])
    cmds.curve( name='thumb2Crv', d=1,p=[(83,152,12),(85, 151, 15)])
    cmds.select(cl=True)
    cmds.skinCluster('thumb1LocJoint','thumb2LocJoint','thumb1Crv',tsb=True)
    cmds.skinCluster('thumb2LocJoint','thumb3LocJoint','thumb2Crv',tsb=True)
    cmds.select(cl=True)
    #Index
    cmds.joint( p=(88,152,7), n='index1LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(91,152,7), n='index2LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(94,151,7), n='index3LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(96,151,7), n='index4LocJoint' )
    cmds.select(clear=True)
    cmds.curve( name='index1Crv', d=1,p=[(88,152,7),(91,152,7)])
    cmds.curve( name='index2Crv', d=1,p=[(91,152,7),(94,151,7)])
    cmds.curve( name='index3Crv', d=1,p=[(94,151,7),(96,151,7)])
    cmds.select(cl=True)
    cmds.skinCluster('index1LocJoint','index2LocJoint','index1Crv',tsb=True)
    cmds.skinCluster('index2LocJoint','index3LocJoint','index2Crv',tsb=True)
    cmds.skinCluster('index3LocJoint','index4LocJoint','index3Crv',tsb=True)
    cmds.select(cl=True)
    #Middle
    cmds.joint( p=(88,152,3.5), n='middle1LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(92,151,3.25), n='middle2LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(95,151,3), n='middle3LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(98,150,3), n='middle4LocJoint' )
    cmds.select(clear=True)
    cmds.curve( name='middle1Crv', d=1,p=[(88,152,3.5),(92,151,3.25)])
    cmds.curve( name='middle2Crv', d=1,p=[(92,151,3.25),(95,151,3)])
    cmds.curve( name='middle3Crv', d=1,p=[(95,151,3),(98,150,3)])
    cmds.select(cl=True)
    cmds.skinCluster('middle1LocJoint','middle2LocJoint','middle1Crv',tsb=True)
    cmds.skinCluster('middle2LocJoint','middle3LocJoint','middle2Crv',tsb=True)
    cmds.skinCluster('middle3LocJoint','middle4LocJoint','middle3Crv',tsb=True)
    cmds.select(cl=True)
    #Ring
    cmds.joint( p=(87,151,1), n='ring1LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(89.5,151,0), n='ring2LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(92.5,151,-.5), n='ring3LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(95,150,-1), n='ring4LocJoint' )
    cmds.select(clear=True)
    cmds.curve( name='ring1Crv', d=1,p=[(87,151,1),(89.5,151,0)])
    cmds.curve( name='ring2Crv', d=1,p=[(89.5,151,0),(92.5,151,-.5)])
    cmds.curve( name='ring3Crv', d=1,p=[(92.5,151,-.5),(95,150,-1)])
    cmds.select(cl=True)
    cmds.skinCluster('ring1LocJoint','ring2LocJoint','ring1Crv',tsb=True)
    cmds.skinCluster('ring2LocJoint','ring3LocJoint','ring2Crv',tsb=True)
    cmds.skinCluster('ring3LocJoint','ring4LocJoint','ring3Crv',tsb=True)
    cmds.select(cl=True)
    #Pinky
    cmds.joint( p=(85,151,-1.5), n='pinky1LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(87,151,-2.5), n='pinky2LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(89,150,-3.5), n='pinky3LocJoint' )
    cmds.select(clear=True)
    cmds.joint( p=(91,150,-4.5), n='pinky4LocJoint' )
    cmds.select(clear=True)
    cmds.curve( name='pinky1Crv', d=1,p=[(85,151,-1.5),(87,151,-2.5)])
    cmds.curve( name='pinky2Crv', d=1,p=[(87,151,-2.5),(89,150,-3.5)])
    cmds.curve( name='pinky3Crv', d=1,p=[(89,150,-3.5),(91,150,-4.5)])
    cmds.select(cl=True)
    cmds.skinCluster('pinky1LocJoint','pinky2LocJoint','pinky1Crv',tsb=True)
    cmds.skinCluster('pinky2LocJoint','pinky3LocJoint','pinky2Crv',tsb=True)
    cmds.skinCluster('pinky3LocJoint','pinky4LocJoint','pinky3Crv',tsb=True)
    cmds.select(cl=True)
def handCreation():
    handPref = cmds.textField('hTF1',q=True,tx=True)
    handSuf = cmds.textField('hTF2',q=True,tx=True)
    ##---------Hand-----Joints
    handJointLoc = cmds.xform('handLocJoint',query=True,ws=True,t=True)
    cmds.joint(n='L_handBndJoint',p=handJointLoc)
    cmds.select(cl=True)
    handJoint= ['thumb','index','middle','ring','pinky']
    thumbJointLoc= ['','','']
    indexJointLoc= ['','','','']
    middleJointLoc= ['','','','']
    ringJointLoc= ['','','','']
    pinkyJointLoc= ['','','','']
    nThumbJointLoc= ['','','']
    nIndexJointLoc= ['','','','']
    nMiddleJointLoc= ['','','','']
    nRingJointLoc= ['','','','']
    nPinkyJointLoc= ['','','','']
    ##------------------Thumb---------------
    for i in range(len(thumbJointLoc)):
        thumbJointLoc[i] = cmds.xform(handJoint[0]+(str(i+1))+'LocJoint',query=True,ws=True,t=True)
    for i in range(len(thumbJointLoc)):
        cmds.joint(n='L_'+handJoint[0]+(str(i+1))+'BndJoint',p=thumbJointLoc[i])
    for i in range(len(thumbJointLoc)):
        cmds.joint('L_'+handJoint[0]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('L_'+handJoint[0]+'3BndJoint.jointOrientX', 0)
    cmds.setAttr('L_'+handJoint[0]+'3BndJoint.jointOrientY', 0)
    cmds.setAttr('L_'+handJoint[0]+'3BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    ##----------------index-------------------
    for i in range(len(indexJointLoc)):
        indexJointLoc[i] = cmds.xform(handJoint[1]+(str(i+1))+'LocJoint',query=True,ws=True,t=True)
    for i in range(len(indexJointLoc)):
        cmds.joint(n='L_'+handJoint[1]+(str(i+1))+'BndJoint',p=indexJointLoc[i])
    for i in range(len(indexJointLoc)):
        cmds.joint('L_'+handJoint[1]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('L_'+handJoint[1]+'4BndJoint.jointOrientX', 0)
    cmds.setAttr('L_'+handJoint[1]+'4BndJoint.jointOrientY', 0)
    cmds.setAttr('L_'+handJoint[1]+'4BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    ##-----------------Middle---------------
    for i in range(len(middleJointLoc)):
        middleJointLoc[i] = cmds.xform(handJoint[2]+(str(i+1))+'LocJoint',query=True,ws=True,t=True)
    for i in range(len(indexJointLoc)):
        cmds.joint(n='L_'+handJoint[2]+(str(i+1))+'BndJoint',p=middleJointLoc[i])
    for i in range(len(indexJointLoc)):
        cmds.joint('L_'+handJoint[2]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('L_'+handJoint[2]+'4BndJoint.jointOrientX', 0)
    cmds.setAttr('L_'+handJoint[2]+'4BndJoint.jointOrientY', 0)
    cmds.setAttr('L_'+handJoint[2]+'4BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    ##---------------Ring-------------------------------
    for i in range(len(indexJointLoc)):
        ringJointLoc[i] = cmds.xform(handJoint[3]+(str(i+1))+'LocJoint',query=True,ws=True,t=True)
    for i in range(len(indexJointLoc)):
        cmds.joint(n='L_'+handJoint[3]+(str(i+1))+'BndJoint',p=ringJointLoc[i])
    for i in range(len(indexJointLoc)):
        cmds.joint('L_'+handJoint[3]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('L_'+handJoint[3]+'4BndJoint.jointOrientX', 0)
    cmds.setAttr('L_'+handJoint[3]+'4BndJoint.jointOrientY', 0)
    cmds.setAttr('L_'+handJoint[3]+'4BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    ##---------------Pinky------------------
    for i in range(len(indexJointLoc)):
        pinkyJointLoc[i] = cmds.xform(handJoint[4]+(str(i+1))+'LocJoint',query=True,ws=True,t=True)
    for i in range(len(indexJointLoc)):
        cmds.joint(n='L_'+handJoint[4]+(str(i+1))+'BndJoint',p=pinkyJointLoc[i])
    for i in range(len(indexJointLoc)):
        cmds.joint('L_'+handJoint[4]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('L_'+handJoint[4]+'4BndJoint.jointOrientX', 0)
    cmds.setAttr('L_'+handJoint[4]+'4BndJoint.jointOrientY', 0)
    cmds.setAttr('L_'+handJoint[4]+'4BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    cmds.delete('thumb1LocJoint','thumb2LocJoint','thumb3LocJoint','thumb1Crv','thumb2Crv')
    cmds.delete('index1LocJoint','index2LocJoint','index3LocJoint','index4LocJoint','index1Crv','index2Crv','index3Crv')
    cmds.delete('middle1LocJoint','middle2LocJoint','middle3LocJoint','middle4LocJoint','middle1Crv','middle2Crv','middle3Crv')
    cmds.delete('ring1LocJoint','ring2LocJoint','ring3LocJoint','ring4LocJoint','ring1Crv','ring2Crv','ring3Crv')
    cmds.delete('pinky1LocJoint','pinky2LocJoint','pinky3LocJoint','pinky4LocJoint','pinky1Crv','pinky2Crv','pinky3Crv')
    cmds.parent('L_'+handJoint[0]+'1BndJoint','L_'+handJoint[1]+'1BndJoint','L_'+handJoint[2]+'1BndJoint','L_'+handJoint[3]+'1BndJoint','L_'+handJoint[4]+'1BndJoint','L_handBndJoint')
    cmds.curve(n='L_hand_ctrl',d=1,p=[(5,0,5),(5,0,-5),(-5,0,-5),(-5,0,5),(5,0,5)],
                                     k=[0,1,2,3,4])
    for i in range(2):
        cmds.addAttr('L_hand_ctrl',ln='L_'+handJoint[0]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('L_hand_ctrl.'+'L_'+handJoint[0]+'_0'+(str(i+1)),keyable=True)
    for i in range(3):
        cmds.addAttr('L_hand_ctrl',ln='L_'+handJoint[1]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('L_hand_ctrl.'+'L_'+handJoint[1]+'_0'+(str(i+1)),keyable=True)
    for i in range(3):
        cmds.addAttr('L_hand_ctrl',ln='L_'+handJoint[2]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('L_hand_ctrl.'+'L_'+handJoint[2]+'_0'+(str(i+1)),keyable=True)
    for i in range(3):
        cmds.addAttr('L_hand_ctrl',ln='L_'+handJoint[3]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('L_hand_ctrl.'+'L_'+handJoint[3]+'_0'+(str(i+1)),keyable=True)
    for i in range(3):
        cmds.addAttr('L_hand_ctrl',ln='L_'+handJoint[4]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('L_hand_ctrl.'+'L_'+handJoint[4]+'_0'+(str(i+1)),keyable=True)
    cmds.addAttr('L_hand_ctrl',ln='____________________',at='double')
    cmds.setAttr('L_hand_ctrl.____________________',e=True,cb=True)
    for i in range(5):
        cmds.addAttr('L_hand_ctrl',ln='L_'+handJoint[i]+'_Spread',at='double',min=-90,max=90,dv=0)
        cmds.setAttr('L_hand_ctrl.'+'L_'+handJoint[i]+'_Spread',keyable=True)
    cmds.group('L_hand_ctrl',n='L_hand_ctrlGrp')
    cmds.parent('L_hand_ctrlGrp','L_handBndJoint',r=True)
    cmds.setAttr("L_hand_ctrlGrp.translateX", 0)
    cmds.setAttr("L_hand_ctrlGrp.translateY", 0)
    cmds.setAttr("L_hand_ctrlGrp.translateZ", 0)
    cmds.parent('L_hand_ctrlGrp',w=True)
    cmds.move(0,5,0,'L_hand_ctrlGrp',r=True,os=True)
    cmds.parentConstraint('L_handBndJoint','L_hand_ctrlGrp',mo=True)
    for i in range(2):
        cmds.connectAttr('L_hand_ctrl.'+'L_'+handJoint[0]+'_0'+(str(i+1)),'L_'+handJoint[0]+(str(i+1))+'BndJoint.rotateY')
    for i in range(3):
        cmds.connectAttr('L_hand_ctrl.'+'L_'+handJoint[1]+'_0'+(str(i+1)),'L_'+handJoint[1]+(str(i+1))+'BndJoint.rotateZ')
    for i in range(3):
        cmds.connectAttr('L_hand_ctrl.'+'L_'+handJoint[2]+'_0'+(str(i+1)),'L_'+handJoint[2]+(str(i+1))+'BndJoint.rotateZ')
    for i in range(3):
        cmds.connectAttr('L_hand_ctrl.'+'L_'+handJoint[3]+'_0'+(str(i+1)),'L_'+handJoint[3]+(str(i+1))+'BndJoint.rotateZ')
    for i in range(3):
        cmds.connectAttr('L_hand_ctrl.'+'L_'+handJoint[4]+'_0'+(str(i+1)),'L_'+handJoint[4]+(str(i+1))+'BndJoint.rotateZ')
    for i in range(4):
        cmds.connectAttr('L_hand_ctrl.'+'L_'+handJoint[i+1]+'_Spread','L_'+handJoint[i+1]+(str(i+1))+'BndJoint.rotateY')
    cmds.connectAttr('L_hand_ctrl.'+'L_'+handJoint[0]+'_Spread','L_'+handJoint[0]+'1BndJoint.rotateZ')
    ##--------------Other----------Hand-----------
    for i in range(len(nThumbJointLoc)):
        negX = thumbJointLoc[i]
        negVal = negX[0]*-1
        negX[0]= negVal
        nThumbJointLoc[i] = negX
    for i in range(len(nIndexJointLoc)):
        negX = indexJointLoc[i]
        negVal = negX[0]*-1
        negX[0]= negVal
        nIndexJointLoc[i] = negX
    for i in range(len(nMiddleJointLoc)):
        negX = middleJointLoc[i]
        negVal = negX[0]*-1
        negX[0]= negVal
        nMiddleJointLoc[i] = negX
    for i in range(len(nRingJointLoc)):
        negX = ringJointLoc[i]
        negVal = negX[0]*-1
        negX[0]= negVal
        nRingJointLoc[i] = negX
    for i in range(len(nPinkyJointLoc)):
        negX = pinkyJointLoc[i]
        negVal = negX[0]*-1
        negX[0]= negVal
        nPinkyJointLoc[i] = negX

    negX = handJointLoc
    negVal = negX[0]*-1
    negX[0]= negVal
    nHandJointLoc = negX
    ##----------------r-Hand------------- 
    cmds.joint(n='R_handBndJoint',p=handJointLoc)
    cmds.select(cl=True)
    ##--------------thumb-------------  
    for i in range(len(thumbJointLoc)):
        cmds.joint(n='R_'+handJoint[0]+(str(i+1))+'BndJoint',p=thumbJointLoc[i])
    for i in range(len(thumbJointLoc)):
        cmds.joint('R_'+handJoint[0]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('R_'+handJoint[0]+'3BndJoint.jointOrientX', 0)
    cmds.setAttr('R_'+handJoint[0]+'3BndJoint.jointOrientY', 0)
    cmds.setAttr('R_'+handJoint[0]+'3BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    ##----------------index-------------------
    for i in range(len(indexJointLoc)):
        cmds.joint(n='R_'+handJoint[1]+(str(i+1))+'BndJoint',p=indexJointLoc[i])
    for i in range(len(indexJointLoc)):
        cmds.joint('R_'+handJoint[1]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('R_'+handJoint[1]+'4BndJoint.jointOrientX', 0)
    cmds.setAttr('R_'+handJoint[1]+'4BndJoint.jointOrientY', 0)
    cmds.setAttr('R_'+handJoint[1]+'4BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    ##-----------------Middle---------------
    for i in range(len(indexJointLoc)):
        cmds.joint(n='R_'+handJoint[2]+(str(i+1))+'BndJoint',p=middleJointLoc[i])
    for i in range(len(indexJointLoc)):
        cmds.joint('R_'+handJoint[2]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('R_'+handJoint[2]+'4BndJoint.jointOrientX', 0)
    cmds.setAttr('R_'+handJoint[2]+'4BndJoint.jointOrientY', 0)
    cmds.setAttr('R_'+handJoint[2]+'4BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    ##---------------Ring-------------------------------
    for i in range(len(indexJointLoc)):
        cmds.joint(n='R_'+handJoint[3]+(str(i+1))+'BndJoint',p=ringJointLoc[i])
    for i in range(len(indexJointLoc)):
        cmds.joint('R_'+handJoint[3]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('R_'+handJoint[3]+'4BndJoint.jointOrientX', 0)
    cmds.setAttr('R_'+handJoint[3]+'4BndJoint.jointOrientY', 0)
    cmds.setAttr('R_'+handJoint[3]+'4BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    ##---------------Pinky------------------
    for i in range(len(indexJointLoc)):
        cmds.joint(n='R_'+handJoint[4]+(str(i+1))+'BndJoint',p=pinkyJointLoc[i])
    for i in range(len(indexJointLoc)):
        cmds.joint('R_'+handJoint[4]+(str(i+1))+'BndJoint',e=True,zso=True,oj='xyz',ch=True,sao='yup')
    cmds.setAttr('R_'+handJoint[4]+'4BndJoint.jointOrientX', 0)
    cmds.setAttr('R_'+handJoint[4]+'4BndJoint.jointOrientY', 0)
    cmds.setAttr('R_'+handJoint[4]+'4BndJoint.jointOrientZ', 0)
    cmds.select(cl=True)
    cmds.parent('R_'+handJoint[0]+'1BndJoint','R_'+handJoint[1]+'1BndJoint','R_'+handJoint[2]+'1BndJoint','R_'+handJoint[3]+'1BndJoint','R_'+handJoint[4]+'1BndJoint','R_handBndJoint')
    cmds.curve(n='R_hand_ctrl',d=1,p=[(5,0,5),(5,0,-5),(-5,0,-5),(-5,0,5),(5,0,5)],
                                     k=[0,1,2,3,4])
    for i in range(2):
        cmds.addAttr('R_hand_ctrl',ln='R_'+handJoint[0]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('R_hand_ctrl.'+'R_'+handJoint[0]+'_0'+(str(i+1)),keyable=True)
    for i in range(3):
        cmds.addAttr('R_hand_ctrl',ln='R_'+handJoint[1]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('R_hand_ctrl.'+'R_'+handJoint[1]+'_0'+(str(i+1)),keyable=True)
    for i in range(3):
        cmds.addAttr('R_hand_ctrl',ln='R_'+handJoint[2]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('R_hand_ctrl.'+'R_'+handJoint[2]+'_0'+(str(i+1)),keyable=True)
    for i in range(3):
        cmds.addAttr('R_hand_ctrl',ln='R_'+handJoint[3]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('R_hand_ctrl.'+'R_'+handJoint[3]+'_0'+(str(i+1)),keyable=True)
    for i in range(3):
        cmds.addAttr('R_hand_ctrl',ln='R_'+handJoint[4]+'_0'+(str(i+1)),at='double',min=-90,max=90,dv=0)
        cmds.setAttr('R_hand_ctrl.'+'R_'+handJoint[4]+'_0'+(str(i+1)),keyable=True)
    cmds.addAttr('R_hand_ctrl',ln='____________________',at='double')
    cmds.setAttr('R_hand_ctrl.____________________',e=True,cb=True)
    for i in range(5):
        cmds.addAttr('R_hand_ctrl',ln='R_'+handJoint[i]+'_Spread',at='double',min=-90,max=90,dv=0)
        cmds.setAttr('R_hand_ctrl.'+'R_'+handJoint[i]+'_Spread',keyable=True)
    cmds.group('R_hand_ctrl',n='R_hand_ctrlGrp')
    cmds.parent('R_hand_ctrlGrp','R_handBndJoint',r=True)
    cmds.setAttr("R_hand_ctrlGrp.translateX", 0)
    cmds.setAttr("R_hand_ctrlGrp.translateY", 0)
    cmds.setAttr("R_hand_ctrlGrp.translateZ", 0)
    cmds.parent('R_hand_ctrlGrp',w=True)
    cmds.move(0,5,0,'R_hand_ctrlGrp',r=True,os=True)
    cmds.parentConstraint('R_handBndJoint','R_hand_ctrlGrp',mo=True)
    for i in range(2):
        cmds.connectAttr('R_hand_ctrl.'+'R_'+handJoint[0]+'_0'+(str(i+1)),'R_'+handJoint[0]+(str(i+1))+'BndJoint.rotateY')
    for i in range(3):
        cmds.connectAttr('R_hand_ctrl.'+'R_'+handJoint[1]+'_0'+(str(i+1)),'R_'+handJoint[1]+(str(i+1))+'BndJoint.rotateZ')
    for i in range(3):
        cmds.connectAttr('R_hand_ctrl.'+'R_'+handJoint[2]+'_0'+(str(i+1)),'R_'+handJoint[2]+(str(i+1))+'BndJoint.rotateZ')
    for i in range(3):
        cmds.connectAttr('R_hand_ctrl.'+'R_'+handJoint[3]+'_0'+(str(i+1)),'R_'+handJoint[3]+(str(i+1))+'BndJoint.rotateZ')
    for i in range(3):
        cmds.connectAttr('R_hand_ctrl.'+'R_'+handJoint[4]+'_0'+(str(i+1)),'R_'+handJoint[4]+(str(i+1))+'BndJoint.rotateZ')
    for i in range(4):
        cmds.connectAttr('R_hand_ctrl.'+'R_'+handJoint[i+1]+'_Spread','R_'+handJoint[i+1]+(str(i+1))+'BndJoint.rotateY')
    cmds.connectAttr('R_hand_ctrl.'+'R_'+handJoint[0]+'_Spread','R_'+handJoint[0]+'1BndJoint.rotateZ')
def combRig():
    cNsp = cmds.textField('characterNameSpace',q=True,tx=True)
    cogJointLoc = cmds.xform('Spine_01_BndJoint',query=True,ws=True,t=True)
    cmds.select(cl=True)
    cmds.select('*_Ctrl')
    Ctrl_list = cmds.ls(sl=True)
    for i in range(len(Ctrl_list)):
        cmds.setAttr(Ctrl_list[i]+'.sx',lock=True,keyable=False,channelBox=False)
        cmds.setAttr(Ctrl_list[i]+'.sy',lock=True,keyable=False,channelBox=False)
        cmds.setAttr(Ctrl_list[i]+'.sz',lock=True,keyable=False,channelBox=False)
        cmds.setAttr(Ctrl_list[i]+'.visibility',lock=True,keyable=False,channelBox=False)
    cmds.select(cl=True)
    cmds.joint(n='cog_ctrlJoint',p=cogJointLoc)
    cmds.select(cl=True)
    cmds.joint(n='cog_BndJoint',p=cogJointLoc)
    cmds.select(cl=True)
    cmds.parent('L_hipBndJoint','R_hipBndJoint','Spine_01_BndJoint','cog_BndJoint')
    cmds.parent('L_hipctrlJoint','R_hipctrlJoint','Spine_01_ctrlJoint','cog_ctrlJoint')
    cmds.parentConstraint('low_Ctrl','cog_ctrlJoint',mo=True)
    cmds.parentConstraint('cog_ctrlJoint','cog_BndJoint',mo=True)
    cmds.parent('L_clavBndJoint','R_clavBndJoint','Spine_05_BndJoint')
    cmds.parent('L_clavFK_joint','R_clavFK_joint','Spine_05_BndJoint')
    cmds.parent('L_clavIK_joint','R_clavIK_joint','Spine_05_BndJoint')
    cmds.parent('L_shoulder_FK_CtrlGrp','R_shoulder_FK_CtrlGrp','topSpine_Null')
    cmds.parent('L_handBndJoint','L_wristBndJoint')
    cmds.parent('R_handBndJoint','R_wristBndJoint')
    cmds.circle(n='Gbl_Ctrl', nr=(0, 1, 0), c=(0, 0, 0) ,r=25.0,ch=False)

    cmds.group('spineIK','spineCtrlCrv',n='no_Touch')
    cmds.select(r=True,ado=True)
    cmds.select('no_Touch','Gbl_Ctrl',d=True)
    inGbl = cmds.ls(sl=True)
    cmds.parent(inGbl,'Gbl_Ctrl')
    cmds.group('no_Touch','Gbl_Ctrl',n=cNsp)
    cmds.shadingNode('multiplyDivide',asUtility=True,n='gblScaleMulDiv')
    curLen = cmds.getAttr('spineCrvInfo.arcLength') 
    cmds.setAttr('gblScaleMulDiv.input1X', curLen)
    cmds.connectAttr('Gbl_Ctrl.scaleX','gblScaleMulDiv.input2X')
    cmds.connectAttr('gblScaleMulDiv.outputX','crvLenMulDiv.input2X')	
