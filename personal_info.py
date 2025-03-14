{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ramnagella/Demo/blob/master/personal_info.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"hello\")"
      ],
      "metadata": {
        "id": "zkA6lDIWMM7H"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "zwFnJsE6vjf8"
      },
      "outputs": [],
      "source": [
        "#personal_info file or module should be saved in ramnagella/demo folder and run it\n",
        "#function should have retrun value otherwise it will give none value\n",
        "name=\"Ram\"\n",
        "def message(name):\n",
        "  return f\"hello,{name}\"\n",
        "  print(f\"hello,{name}\")\n",
        "def addition(a,b):\n",
        "  return a+b\n",
        "PI=3.14159\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import personal_info\n",
        "personal_info.message(\"ram\")"
      ],
      "metadata": {
        "id": "sJTJLsBlZEi8",
        "outputId": "3a24e62d-cc22-4136-f232-61ec91e09caa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 332
        }
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'personal_info'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-270bd0f1e0ca>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mpersonal_info\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mpersonal_info\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"ram\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'personal_info'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome to Colaboratory",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}