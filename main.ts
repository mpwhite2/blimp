namespace SpriteKind {
    export const Pewpew = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
        4 4 
        4 4 
        4 4 
        `, mySprite, 0, 150)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
    projectile.setBounceOnWall(true)
    timer.after(50, function () {
        projectile.setKind(SpriteKind.Pewpew)
    })
})
sprites.onOverlap(SpriteKind.Pewpew, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy(effects.fire, 500)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Pewpew, function (sprite, otherSprite) {
    game.over(false)
})
let Blimp: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.setPosition(80, 9)
controller.moveSprite(mySprite, 100, 0)
info.setScore(0)
mySprite.setStayInScreen(true)
game.onUpdateInterval(100, function () {
    if (Math.percentChance(5)) {
        Blimp = sprites.createProjectileFromSide(img`
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
            `, randint(1, 100), 0)
        Blimp.setPosition(0, randint(20, 120))
        Blimp.setKind(SpriteKind.Enemy)
    }
})
