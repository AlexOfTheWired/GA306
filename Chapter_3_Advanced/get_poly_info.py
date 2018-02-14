import maya.cmds as mc


def get_poly_info(m_sel=mc.ls(selection=True)):
    p_info = mc.polyEvaluate(f=True,e=True,v=True)
    print(p_info)