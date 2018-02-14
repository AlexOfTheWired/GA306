import maya.cmds as mc

def find_center(m_sel=mc.ls(selection=True)):
    
    x_pos = 0
    y_pos = 0
    z_pos = 0
    
    vert_num = mc.polyEvaluate(v=True)
    
    for vert in range(vert_num):
        ws_pos= mc.xform('%s.vtx%s' % (m_sel[0],[vert]),q=True,ws=True,t=True)

        x_pos += ws_pos[0]
        y_pos += ws_pos[1]
        z_pos += ws_pos[2]   
        
        x_pos_average = x_pos / vert_num
        y_pos_average = y_pos / vert_num
        z_pos_average = z_pos / vert_num
           
    print('X: %.3f, Y: %.3f, Z: %.3f' % (x_pos_average, y_pos_average, z_pos_average))