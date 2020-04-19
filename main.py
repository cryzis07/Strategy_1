import style
import fighter

player1 = fighter.Zmey(name='Тугарин', fighting_style=style.Cheshuya())
player2 = fighter.Chelovek(name='Добрыня', fighting_style=style.KulachniiBoi())

player1.attack(player1,player2)
player2.defend(player2,player1)