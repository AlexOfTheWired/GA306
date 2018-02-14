import maya.cmds as mc

def geomotry_filter(m_sel=mc.ls(selection=True),num_filter=100):
    
    new_obj_list = []
    
    for obj in range(len(m_sel)):
        face_num = mc.polyEvaluate(m_sel[obj], f=True)
        if face_num >= num_filter:
            new_obj_list.append(m_sel[obj])
    
def new_geomotry_filter(m_sel=mc.ls(selection=True),num_filter=100):    
    
    new_obj_list = [m_sel[i] for i in range(len(m_sel)) if mc.polyEvaluate(m_sel[i],f=True) >= num_filter]
    mc.select(new_obj_list)