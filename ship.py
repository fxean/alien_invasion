import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船并完成初始设置"""
        self.screen = screen
        # 加载飞船图形并获取其外接矩形

        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(
            self.image,
            (self.image.get_width() / 4, self.image.get_height() / 4)
        )
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕中央底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
