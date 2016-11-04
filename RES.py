from pico2d import *

res = None

def load_resource():
    global res
    res = Res()

class Res:

    #로고 이미지
    logo_image = None

    #타이틀 이미지
    title_image = None

    #스코어 이미지
    score_image = None

    #배경 이미지
    Background_image = None

    #캐릭터 이미지
    Player_image = None

    #장애물 이미지
    First_Obstacle = None
    Second_Obstacle = None

    #발판 이미지
    FBrickImage = None
    SBrickImage = None
    TBrickImage = None
    FOBrickImage = None
    FloatingImage_one = None
    FloatingImage_two = None
    FCloud = None
    SCloud = None

    # 파도 이미지
    Wave_image = None

    # 돌고래 이미지
    dolpin_image = None

    # 메소 이미지
    bronze_meso_image = None
    Big_bronze_meso_image = None

    silver_meso_image = None
    Big_silver_meso_image = None

    gold_meso_image = None
    Big_gold_meso_image = None

    def __init__(self):
        #배경 이미지 로드
        self.Background_image = load_image('Resources/Images/Background/FirstStage_s.png')

        #캐릭터 이미지 로드
        self.Player_image = load_image('Resources/Images/Character/character_sprite.png')

        #포인트 이미지 로드
        self.bronze_meso_image = load_image('Resources/Images/Object/Point/bronze_meso.png')
        self.silver_meso_image = load_image('Resources/Images/Object/Point/silver_meso.png')
        self.gold_meso_image = load_image('Resources/Images/Object/Point/gold_meso.png')

        #스테이지 오브젝트 이미지 로드
        self.dolpin_image = load_image('Resources/Images/Object/Stageobject/Dolpin.png')
        self.Wave_image = load_image('Resources/Images/Object/Stageobject/Wave.png')

        #장애물 이미지 로드
        self.First_Obstacle = load_image('Resources/Images/Obstacle/Obstacle01.png')
        self.Second_Obstacle = load_image('Resources/Images/Obstacle/Obstacle02.png')

        #씬 이미지 로드
        self.logo_image = load_image('Resources/Images/Scene/WarpLogo.png')
        self.title_image = load_image('Resources/Images/Scene/title_logo.png')
        self.score_image = load_image('Resources/Images/Scene/blackboard.png')

        #발판 이미지 로드
        self.FBrickImage = load_image('Resources/Images/Tile/Brick_First.png')
        self.SBrickImage = load_image('Resources/Images/Tile/Brick_Second.png')
        self.TBrickImage = load_image('Resources/Images/Tile/Brick_Third.png')
        self.FOBrickImage = load_image('Resources/Images/Tile/Brick_Fourth.png')
        self.FloatingImage_one = load_image('Resources/Images/Tile/Floating_one.png')
        self.FloatingImage_two = load_image('Resources/Images/Tile/Floating_two.png')
        self.FCloud = load_image('Resources/Images/Tile/Cloud_one.png')
        self.SCloud = load_image('Resources/Images/Tile/Cloud_two.png')


