{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOlUrJ8bYoMr7cP+4N7vvQk",
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
        "<a href=\"https://colab.research.google.com/github/shahd1995913/Arabic-Corrector/blob/main/app_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip install colorama"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sj8t3bGufA48",
        "outputId": "6dc75ac8-4d36-41f1-be30-40e1c53f5d5b"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting colorama\n",
            "  Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)\n",
            "Installing collected packages: colorama\n",
            "Successfully installed colorama-0.4.6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip install streamlit\n",
        "import streamlit as st\n",
        "from colorama import Fore, Back, Style\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ineXrbILgP8R",
        "outputId": "f37474ec-2763-41a2-b968-8654491e604f"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.22.0-py2.py3-none-any.whl (8.9 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.9/8.9 MB\u001b[0m \u001b[31m103.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: altair<5,>=3.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Collecting blinker>=1.0.0 (from streamlit)\n",
            "  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.3)\n",
            "Collecting importlib-metadata>=1.4 (from streamlit)\n",
            "  Downloading importlib_metadata-6.6.0-py3-none-any.whl (22 kB)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.22.4)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (23.1)\n",
            "Requirement already satisfied: pandas<3,>=0.25 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.5.3)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.4.0)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Collecting pympler>=0.9 (from streamlit)\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m164.8/164.8 kB\u001b[0m \u001b[31m20.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.27.1)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.3.4)\n",
            "Requirement already satisfied: tenacity<9,>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.2.2)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.5.0)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.3)\n",
            "Collecting validators>=0.2 (from streamlit)\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting gitpython!=3.1.19 (from streamlit)\n",
            "  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m184.3/184.3 kB\u001b[0m \u001b[31m22.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pydeck>=0.1.dev5 (from streamlit)\n",
            "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m117.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.1)\n",
            "Collecting watchdog (from streamlit)\n",
            "  Downloading watchdog-3.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.1/82.1 kB\u001b[0m \u001b[31m11.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (3.1.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.12.0)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19->streamlit)\n",
            "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m7.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata>=1.4->streamlit) (3.15.0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=0.25->streamlit) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil->streamlit) (1.16.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (3.4)\n",
            "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.14.0)\n",
            "Requirement already satisfied: pytz-deprecation-shim in /usr/local/lib/python3.10/dist-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit)\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<5,>=3.2.0->streamlit) (2.1.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (23.1.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (0.19.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.10/dist-packages (from pytz-deprecation-shim->tzlocal>=1.1->streamlit) (2023.3)\n",
            "Building wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19579 sha256=74464994586640339a51e481340d67bf7de820179ed4af0de62e4237ae997fb5\n",
            "  Stored in directory: /root/.cache/pip/wheels/f2/ed/dd/d3a556ad245ef9dc570c6bcd2f22886d17b0b408dd3bbb9ac3\n",
            "Successfully built validators\n",
            "Installing collected packages: watchdog, validators, smmap, pympler, importlib-metadata, blinker, pydeck, gitdb, gitpython, streamlit\n",
            "Successfully installed blinker-1.6.2 gitdb-4.0.10 gitpython-3.1.31 importlib-metadata-6.6.0 pydeck-0.8.1b0 pympler-1.0.1 smmap-5.0.0 streamlit-1.22.0 validators-0.20.0 watchdog-3.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1vtDkMwVe-Pi",
        "outputId": "c0786b80-c0a1-4d5d-85b2-e186312b0fe1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2023-05-15 13:00:36.758 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ],
      "source": [
        "import streamlit as st\n",
        "from colorama import Fore, Back, Style\n",
        "\n",
        "# Print colored text\n",
        "st.text(Fore.GREEN + 'some red text')\n",
        "\n",
        "# Styling functions for colored and bold text\n",
        "def blue(text):\n",
        "    return f\"<span style='color: blue;'>{text}</span>\"\n",
        "\n",
        "def green(text):\n",
        "    return f\"<span style='color: green;'>{text}</span>\"\n",
        "\n",
        "# Get user input\n",
        "text = st.text_input(\"الرجاء إدخال النص المراد تدقيقه\")\n",
        "\n",
        "# Perform replacements\n",
        "text2 = text.replace(\"زرتو\", \"زرت\")\n",
        "text2 = text2.replace(\"درستو\", \"درست\")\n",
        "text2 = text2.replace(\"دائمن\", \"دائما\")\n",
        "text2 = text2.replace(\"الاستاذ\", \"الأستاذ\")\n",
        "text2 = text2.replace(\"مسائا\", \"مساءً\")\n",
        "text2 = text2.replace(\"هبه\", \"هبة\")\n",
        "text2 = text2.replace(\"دعى\", \"دعا\")\n",
        "\n",
        "# Display original and corrected text\n",
        "st.markdown('**النص قبل التصحيح:** ' + blue(text))\n",
        "st.markdown('**النص بعد التصحيح:** ' + green(text2))\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "i4dWo9wigQIr"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}