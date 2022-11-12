@namespace
class SpriteKind:
    Pewpew = SpriteKind.create()

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            4 4 
                    4 4 
                    4 4
        """),
        mySprite,
        0,
        150)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
    projectile.set_bounce_on_wall(True)
    
    def on_after():
        projectile.set_kind(SpriteKind.Pewpew)
    timer.after(50, on_after)
    
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.fire, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.Pewpew, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.Pewpew, on_on_overlap2)

Blimp: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
            . . 7 7 7 7 7 7 7 7 7 7 7 7 . . 
            . . . 7 7 7 7 7 7 7 7 7 7 . . . 
            . . . . 7 7 7 7 7 7 7 7 . . . . 
            . . . . . . 7 7 7 7 . . . . . . 
            . . . . . . . 7 7 . . . . . . . 
            . . . . . . . 7 7 . . . . . . . 
            . . . . . . . 7 7 . . . . . . . 
            . . . . . . . 7 7 . . . . . . . 
            . . . . . . . 7 7 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite.set_position(80, 9)
controller.move_sprite(mySprite, 100, 0)
info.set_score(0)
mySprite.set_stay_in_screen(True)

def on_update_interval():
    global Blimp
    if Math.percent_chance(5):
        Blimp = sprites.create_projectile_from_side(img("""
                . . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . . 
                            . e . . . . . . 1 1 1 1 1 1 1 . . . . . 
                            . e e . . . 1 1 1 1 1 1 1 1 1 1 1 . . . 
                            . e e e 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 . 
                            . e 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                            . e e e 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 . 
                            . e e . . . 1 1 1 1 1 1 1 1 1 1 1 . . . 
                            . e . . . . . . 1 1 1 1 1 1 1 1 . . . . 
                            . . . . . . . . . . . e e e e . . . . . 
                            . . . . . . . . . . . e e e e . . . . . 
                            . . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . .
            """),
            randint(1, 100),
            0)
        Blimp.set_position(0, randint(20, 120))
        Blimp.set_kind(SpriteKind.enemy)
game.on_update_interval(100, on_update_interval)
