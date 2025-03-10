{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyNVd3QwqNq2NRHkBh3RxZpu",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/6758074256/Run_Eng/blob/main/Thaicons.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Aux1Ek02FkBD"
      },
      "outputs": [],
      "source": [
        "import tkinter as tk\n",
        "import random\n",
        "\n",
        "# List of Thai consonants and their names\n",
        "thai_consonants = [\n",
        "    (\"ก\", \"Gor Gai (กอ ไก่)\"),\n",
        "    (\"\\u0e02\", \"Kho Khai (ขอ ไข่)\"),\n",
        "    (\"\\u0e04\", \"Kho Khuat (คอ ควาย)\"),\n",
        "    (\"\\u0e06\", \"Kho Rakhang (ฆอ ระฆํง)\"),\n",
        "    (\"\\u0e08\", \"Cho Ching (ฉอ ฉิ่ง)\"),\n",
        "    (\"\\u0e0a\", \"Cho Chang (ชอ ช้าง)\"),\n",
        "    (\"\\u0e0d\", \"Yo Ying (ญอ หญิง)\"),\n",
        "    (\"\\u0e10\", \"Tho Thahan (ฐอ ฐาน)\"),\n",
        "    (\"\\u0e14\", \"Do Dek (ดอ เด็ก)\"),\n",
        "    (\"\\u0e16\", \"Tho Thong (ถอ ถุง)\")\n",
        "]\n",
        "\n",
        "class FlashcardGame:\n",
        "    def __init__(self, root):\n",
        "        self.root = root\n",
        "        self.root.title(\"Thai Consonant Flashcard Game\")\n",
        "        self.current_card = None\n",
        "\n",
        "        self.canvas = tk.Canvas(root, width=400, height=300, bg=\"white\")\n",
        "        self.canvas.pack()\n",
        "\n",
        "        self.card_text = self.canvas.create_text(200, 150, text=\"\", font=(\"Arial\", 50, \"bold\"))\n",
        "\n",
        "        self.flip_button = tk.Button(root, text=\"Flip Card\", command=self.flip_card)\n",
        "        self.flip_button.pack()\n",
        "\n",
        "        self.next_button = tk.Button(root, text=\"Next Card\", command=self.next_card)\n",
        "        self.next_button.pack()\n",
        "\n",
        "        self.next_card()\n",
        "\n",
        "    def next_card(self):\n",
        "        self.current_card = random.choice(thai_consonants)\n",
        "        self.canvas.itemconfig(self.card_text, text=self.current_card[0])\n",
        "        self.flipped = False\n",
        "\n",
        "    def flip_card(self):\n",
        "        if self.current_card:\n",
        "            if not self.flipped:\n",
        "                self.canvas.itemconfig(self.card_text, text=self.current_card[1])\n",
        "                self.flipped = True\n",
        "            else:\n",
        "                self.canvas.itemconfig(self.card_text, text=self.current_card[0])\n",
        "                self.flipped = False\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    root = tk.Tk()\n",
        "    game = FlashcardGame(root)\n",
        "    root.mainloop()"
      ]
    }
  ]
}
