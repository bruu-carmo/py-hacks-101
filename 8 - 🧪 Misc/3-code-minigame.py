import random

class CodeGame:
    def __init__(self, secret_code=None, language='en'):
        self.secret_code = secret_code if secret_code else random.sample(range(10), 3)
        self.language = language
        self.text = self.load_text()

    def load_text(self):
        return {
            'en': {
                'welcome': "🎯 Welcome to the Code Breaker Game!",
                'instructions': "Try to guess the 3-digit code. Digits are unique.",
                'exit_tip': "Type 'exit' to quit.\n",
                'prompt': "Enter a 3-digit code guess: ",
                'exit_msg': "👋 Game exited. Thanks for playing!",
                'invalid': "⚠️ Invalid input. Enter exactly 3 digits.\n",
                'feedback': "📊 Feedback: {} well placed, {} misplaced.\n",
                'win': "🎉 Congratulations! You broke the code in {} attempts.",
                'answer': "✅ Secret code was: {}"
            },
            'pt': {
                'welcome': "🎯 Bem-vindo ao Jogo Quebra-Código!",
                'instructions': "Tente adivinhar o código de 3 dígitos. Os dígitos são únicos.",
                'exit_tip': "Digite 'exit' para sair.\n",
                'prompt': "Digite seu palpite (3 dígitos): ",
                'exit_msg': "👋 Jogo encerrado. Obrigado por jogar!",
                'invalid': "⚠️ Entrada inválida. Digite exatamente 3 dígitos.\n",
                'feedback': "📊 Dica: {} correto(s) e bem colocado(s), {} no lugar errado.\n",
                'win': "🎉 Parabéns! Você descobriu o código em {} tentativas.",
                'answer': "✅ O código era: {}"
            }
        }[self.language]

    def get_feedback(self, guess):
        guess_digits = [int(d) for d in guess]
        well_placed = sum([1 for i in range(3) if guess_digits[i] == self.secret_code[i]])
        misplaced = sum([1 for d in guess_digits if d in self.secret_code]) - well_placed
        return well_placed, misplaced

    def play(self):
        print(self.text['welcome'])
        print(self.text['instructions'])
        print(self.text['exit_tip'])

        attempts = 0
        while True:
            guess = input(self.text['prompt']).strip()

            if guess.lower() == "exit":
                print(self.text['exit_msg'])
                break

            if not guess.isdigit() or len(guess) != 3:
                print(self.text['invalid'])
                continue

            attempts += 1
            well_placed, misplaced = self.get_feedback(guess)

            print(self.text['feedback'].format(well_placed, misplaced))

            if well_placed == 3:
                print(self.text['win'].format(attempts))
                print(self.text['answer'].format(''.join(str(d) for d in self.secret_code)))
                break


if __name__ == "__main__":
    print("1 - Português 🇧🇷")
    print("2 - English 🇺🇸")
    lang_option = input("Escolha o idioma / Choose your language: ").strip()

    language = 'pt' if lang_option == '1' else 'en'
    game = CodeGame(secret_code=[0, 4, 2], language=language)
    game.play()