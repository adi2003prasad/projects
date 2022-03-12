class cake():
    def __init__(self, rows, columns, cut_length) -> None:
        self.max_cut = cut_length
        self.rows = rows
        self.columns = columns
    def coordinates_maker(self):
        rows = self.rows
        columns = self.columns
        self.dictionary_of_plane_boundaries = {}
        for x in range(1, rows+1):
            for y in range(1, columns+1):
                if((x==1 and y==1)or(x==(rows) and y==(rows))or(x==(rows) and y==1)or(x==1 and y==(rows))):
                    self.dictionary_of_plane_boundaries[(x, y)] = self.dictionary_of_plane_boundaries.get((x, y), 0)+2
                elif(x==1 or y==1 or x==(rows) or y==(columns)):
                    self.dictionary_of_plane_boundaries[(x, y)] = self.dictionary_of_plane_boundaries.get((x, y), 0)+3
                else:
                    self.dictionary_of_plane_boundaries[(x, y)] = self.dictionary_of_plane_boundaries.get((x, y), 0)+4
        return(self.dictionary_of_plane_boundaries)
    def tasty_area(self, start_r, start_c, end_r, end_C):
        self.tasty_area_of_cake = [(int(start_r), int(start_c)), (int(end_r), int(end_C))]
        return self.tasty_area_of_cake
    def cut(self, box_coordinate, cut_dir):
        '''
        the box_cordinate describes the box around which the cut should take place\n
        the cut_dir describes the cut direction from the center of box, \n
        cut_dir should be as follows\n
        0 - up\n
        1 - right\n
        2 - down\n
        3 - left\n
        
        '''
        world_current = self.dictionary_of_plane_boundaries
        if(box_coordinate[0]==1):
            if(cut_dir==0):
                return "cut can't be done you fool"
        elif(box_coordinate[1]==1):
            if(cut_dir==3):
                return "cut can't be done you fool"   
        elif(box_coordinate[0]==(self.rows)):
            if(cut_dir==2):
                return "cut can't be done you fool"
        elif(box_coordinate[0]==(self.columns)):
            if(cut_dir==1):
                return "cut can't be done you fool"
        else:
            world_current[box_coordinate]-=1
            if(cut_dir==0) : 
                neighbour_coord = (box_coordinate[0]-1, box_coordinate[1])
                world_current[neighbour_coord]-=1

            elif(cut_dir==1) : 
                neighbour_coord = (box_coordinate[0], box_coordinate[1]+1)
                world_current[neighbour_coord]-=1
                
            elif(cut_dir==2) : 
                neighbour_coord = (box_coordinate[0]+1, box_coordinate[1])
                world_current[neighbour_coord]-=1

            elif(cut_dir==3) : 
                neighbour_coord = (box_coordinate[0], box_coordinate[1]-1)
                world_current[neighbour_coord]-=1
            else:
                return "you are a fool"
            self.dictionary_of_plane_boundaries = world_current
            return True
    def is_valid_coordinate(self, coordinate_case):
        if(coordinate_case[0]>self.rows or coordinate_case[0]<1):
            return False
        elif(coordinate_case[1]>self.columns or coordinate_case[1]<1):
            return False
        else:
            return True
    def cutter(self, cut_start, cut_length, cut_direction):
        if(cut_length>self.max_cut):
            return"you cant come here fool"
        
        if(cut_direction==0) : 
            cut_end = (cut_start[0]-cut_length, cut_start[1])
        if(cut_direction==1) : 
            cut_end = (cut_start[0], cut_start[1]+cut_length)
        if(cut_direction==2) : 
            cut_end = (cut_start[0]+cut_length, cut_start[1])
        if(cut_direction==3) : 
            cut_end = (cut_start[0]-cut_length, cut_start[1]-cut_length)


        if not (self.is_valid_coordinate(cut_end)):
            return "cut not possible"
        else:
            curr_coord = cut_start
            for x in range(cut_length):
                self.cut(curr_coord, cut_direction)
                if(cut_direction==0) : 
                    curr_coord = (curr_coord[0]-1, curr_coord[1])
                if(cut_direction==1) : 
                    curr_coord = (curr_coord[0], curr_coord[1]+1)
                if(cut_direction==2) : 
                    curr_coord = (curr_coord[0]+1, curr_coord[1])
                if(cut_direction==3) : 
                    curr_coord = (curr_coord[0], curr_coord[1]-1)
        return self.dictionary_of_plane_boundaries

        


t = int(input(""))
for x in range(t):
    system = input("").split()
    f_cake = cake(int(system[0]), int(system[1]), int(system[2]))
    f_cake.coordinates_maker()
    good_area = input("").split()
    f_cake.tasty_area(good_area[0], good_area[1], good_area[2], good_area[3])
    print(f_cake.cutter((1, 1), 3, 1))
    print(f_cake.dictionary_of_plane_boundaries)





