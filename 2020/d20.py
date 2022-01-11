import itertools
import numpy as np
from math import prod, sqrt

with open('2020/input.txt','r') as file:
    input = file.read().split('\n\n')
    images = {}
    for im in input:
        im = im.splitlines()
        images[im[0].strip().split()[1][:-1]] = im[1:]
    
    images = {k:np.array([np.array(list(a)) for a in v]) for k,v in images.items()}

def get_8_orient(image):
    vars = [image]
    vars.append(np.rot90(image,1))
    vars.append(np.rot90(image,2))
    vars.append(np.rot90(image,3))
    fliped = np.fliplr(image)
    vars.append(fliped)
    vars.append(np.rot90(fliped,1))
    vars.append(np.rot90(fliped,2))
    vars.append(np.rot90(fliped,3))
    return vars

def have_common_border(img1, img2):
    img1_borders = [img1[0,:], img1[:,-1],img1[-1,:],img1[:,0]]
    img2_borders = [img2[0,:], img2[:,-1],img2[-1,:],img2[:,0]]
    for b1 in img1_borders:
        for b2 in img2_borders:
            if np.array_equal(b1,b2):
                return True
    
def find_corners():
    corners = []
    for img1 in images:
        border_count = 0
        img1_orients = get_8_orient(images[img1])
        for img2 in [im2 for im2 in images if im2 != img1]:  
            img2_orients = get_8_orient(images[img2])
            
            if any([have_common_border(im1,im2) for im1,im2 in itertools.product(img1_orients, img2_orients)]):
                border_count += 1

        if border_count == 2:
            corners.append(img1)
    return corners

def part1():
    corners =  find_corners()               
    print('4 corner images:', corners)

    print('Part1:', prod([int(a) for a in corners]))
    
# ----------------------------------------------------------------------

class ImageTile:
    def __init__(self, id, image_array) -> None:
        self.id = id
        self.data = image_array
        self.orients = get_8_orient(image_array)
        self.correct_orient = None
        self.is_finded_correct_orient = False
        self.neighbors = {'up':None, 'right':None, 'down':None, 'left':None}
        
    def get_img_orients(self):
        if self.is_finded_correct_orient:
            return [self.correct_orient]
        else:
            return self.orients
        
    def check_common_border(self, image_tile2):
        img1_oris = self.get_img_orients()
        img2_oris = image_tile2.get_img_orients()
         
        for img1 in img1_oris:
            for img2 in img2_oris:
                flg = False
                if np.array_equal(img1[0,:], img2[-1,:]):
                    self.neighbors['up'] = image_tile2.id
                    image_tile2.neighbors['down'] = self.id
                    flg = True
                    
                if np.array_equal(img1[:,-1], img2[:,0]):
                    self.neighbors['right'] = image_tile2.id
                    image_tile2.neighbors['left'] = self.id
                    flg = True
                    
                if np.array_equal(img1[-1,:], img2[0,:]):
                    self.neighbors['down'] = image_tile2.id
                    image_tile2.neighbors['up'] = self.id
                    flg = True
                    
                if np.array_equal(img1[:,0], img2[:,-1]):
                    self.neighbors['left'] = image_tile2.id
                    image_tile2.neighbors['right'] = self.id
                    flg = True

                if flg:
                    self.correct_orient = img1
                    image_tile2.correct_orient = img2
                    self.is_finded_correct_orient = True
                    image_tile2.is_finded_correct_orient = True
                    return True
                    
def part2(images):        
    images = {k:ImageTile(k,v) for k,v in images.items()}

    while not all([im.is_finded_correct_orient for im in images.values()]):
        for im1, im2 in itertools.permutations(images.values(), 2):
            if ((im1.id == list(images)[0] and not im1.is_finded_correct_orient) or 
                    (im1.is_finded_correct_orient and 
                    not im2.is_finded_correct_orient)):
                im1.check_common_border(im2)

    board_sh = int(sqrt(len(images)))
    board = np.zeros((3*board_sh,3*board_sh), dtype=object)
    images_lst = list(images)
    im1 = images_lst.pop()
    board[int(board.shape[0]/2),int(board.shape[1]/2)] = im1
    seen = set()

    while sum([1 for a in board.flatten() if a != 0]) != len(images):
        for i,j in itertools.product(range(len(board)), repeat=2):
            if (id := board[i,j]) and (board[i,j] not in seen):
                neighs = images[id].neighbors
                for k,v in neighs.items():
                    if v:
                        if k == 'up':
                            board[i-1,j] = v
                        elif k == 'down':
                            board[i+1,j] = v
                        elif k == 'left':
                            board[i,j-1] = v
                        elif k == 'right':
                            board[i,j+1] = v

                seen.add(id)
                
    final_board_id = board[board != 0].reshape((board_sh, board_sh))

    all_rows = []
    for row in final_board_id:
        board_row = images[row[0]].correct_orient[1:-1,1:-1]
        for col in row[1:]:
            board_row = np.hstack((board_row, images[col].correct_orient[1:-1,1:-1]))
        all_rows.append(board_row)

    final_board_data = all_rows[0]
    for row in all_rows[1:]:
        final_board_data = np.vstack((final_board_data, row))
        


    final_board_data = np.flipud(final_board_data)
    sea_monster = '                  # \n#    ##    ##    ###\n #  #  #  #  #  #   '.splitlines()
    sea_monster = [list(a) for a in sea_monster]
    sea_monster = np.array(sea_monster, dtype=object)
    to_check = sea_monster == '#'
    c = 0

    for b in get_8_orient(final_board_data):
        for i in range(0, b.shape[0]-to_check.shape[0]):
            for j in range(0, b.shape[1]-to_check.shape[1]):
                if all(b[i:i+to_check.shape[0], j:j+to_check.shape[1]][to_check] == '#'):
                    c += 1
        if c:
            break
        
    print('Part2:', len(final_board_data[final_board_data == '#']) - c * len(sea_monster[sea_monster == '#']))
    
part1()    
part2(images)