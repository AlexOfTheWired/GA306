def find_center(m_sel=mc.ls(sl=True)):
    result = [0.0, 0.0, 0.0] 
    
    num_verts = mc.polyEvaluate(geo, vertex=True)
    for idx in xrange(num_verts):
        vert_position = mc.xform('%s.vtx[%d]' % (m_sel, idx), q=True, ws=True, t=True)
        for i in range(3):
            result[i] += vert_position[i]
            
    for i in range(3):
        result[i] /= num_verts
        
    return result