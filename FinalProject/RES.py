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

    #메인로비 이미지
    main_lobby = None

    #스코어 이미지
    score_image = None

    #노래 로딩이미지
    first_song = None

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

    #바 이미지
    pinkbin_bar = None
    sky_bar = None
    flying_object_bar = None
    stop_station = None

    #버튼 이미지
    a_button = None
    s_button = None
    d_button = None
    f_button = None
    boom_button = None
    b_button = None

    #콤모 이미지
    Combo = None

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
        self.main_lobby = load_image('Resources/Images/Scene/mainlobby.png')
        self.first_song = load_image('Resources/Images/Scene/FirstSong.png')

        #발판 이미지 로드
        self.FBrickImage = load_image('Resources/Images/Tile/Brick_First.png')
        self.SBrickImage = load_image('Resources/Images/Tile/Brick_Second.png')
        self.TBrickImage = load_image('Resources/Images/Tile/Brick_Third.png')
        self.FOBrickImage = load_image('Resources/Images/Tile/Brick_Fourth.png')
        self.FloatingImage_one = load_image('Resources/Images/Tile/Floating_one.png')
        self.FloatingImage_two = load_image('Resources/Images/Tile/Floating_two.png')
        self.FCloud = load_image('Resources/Images/Tile/Cloud_one.png')
        self.SCloud = load_image('Resources/Images/Tile/Cloud_two.png')

        #바 이미지 로드
        self.sky_bar = load_image('Resources/Images/Upbar/skybar.png')
        self.pinkbin_bar = load_image('Resources/Images/Upbar/pinkbin_bar_mod.png')
        self.flying_object_bar = load_image('Resources/Images/Upbar/FlyingObject02_mod.png')
        self.stop_station = load_image('Resources/Images/Upbar/ButtonStop.png')

        #버튼 이미지 로드
        self.A_button = load_image('Resources/Images/Button/AButton.png')
        self.S_button = load_image('Resources/Images/Button/SButton.png')
        self.D_button = load_image('Resources/Images/Button/DButton.png')
        self.F_button = load_image('Resources/Images/Button/FButton.png')
        self.B_button = load_image('Resources/Images/Button/Bonus_Button.png')
        self.boom_button = load_image('Resources/Images/Button/Boom_Button.png')

        #콤보 이미지 로드
        self.Combo = load_image('Resources/Images/Combo/combo_mod.png')


