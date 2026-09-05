import random

import streamlit as st


# --------------------------------------------------
# 페이지 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="가위바위보 챌린지",
    page_icon="✊",
    layout="centered",
)


# --------------------------------------------------
# 선택지와 게임 규칙
# --------------------------------------------------
CHOICES = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋",
}

WINNING_RULES = {
    "가위": "보",
    "바위": "가위",
    "보": "바위",
}


# --------------------------------------------------
# 세션 상태 초기화
# --------------------------------------------------
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = None

if "result" not in st.session_state:
    st.session_state.result = None

if "wins" not in st.session_state:
    st.session_state.wins = 0

if "losses" not in st.session_state:
    st.session_state.losses = 0

if "draws" not in st.session_state:
    st.session_state.draws = 0


# --------------------------------------------------
# 게임 관련 함수
# --------------------------------------------------
def play_game(user_choice):
    """사용자의 선택을 받아 가위바위보 게임을 진행합니다."""
    computer_choice = random.choice(list(CHOICES.keys()))

    if user_choice == computer_choice:
        result = "draw"
        st.session_state.draws += 1
    elif WINNING_RULES[user_choice] == computer_choice:
        result = "win"
        st.session_state.wins += 1
    else:
        result = "lose"
        st.session_state.losses += 1

    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice
    st.session_state.result = result


def reset_game():
    """게임 기록을 초기화합니다."""
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.result = None
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0


# --------------------------------------------------
# 화면 디자인
# --------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(
                    circle at top left,
                    rgba(70, 120, 255, 0.16),
                    transparent 35%
                ),
                radial-gradient(
                    circle at bottom right,
                    rgba(132, 78, 255, 0.15),
                    transparent 35%
                ),
                #f6f8fc;
        }

        .block-container {
            max-width: 850px;
            padding-top: 2.5rem;
            padding-bottom: 3rem;
        }

        .main-title {
            color: #17223b;
            font-size: 2.6rem;
            font-weight: 900;
            text-align: center;
            margin-bottom: 0.3rem;
        }

        .subtitle {
            color: #65708a;
            font-size: 1.05rem;
            text-align: center;
            margin-bottom: 2rem;
        }

        .score-board {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin: 1.2rem 0 2rem;
        }

        .score-item {
            min-width: 105px;
            padding: 12px 15px;
            border: 1px solid #e2e7f0;
            border-radius: 16px;
            background-color: rgba(255, 255, 255, 0.92);
            box-shadow: 0 6px 20px rgba(36, 48, 80, 0.08);
            color: #303b55;
            text-align: center;
        }

        .score-label {
            color: #747f98;
            font-size: 0.85rem;
            font-weight: 700;
        }

        .score-number {
            margin-top: 3px;
            color: #17223b;
            font-size: 1.5rem;
            font-weight: 900;
        }

        .section-title {
            color: #303b55;
            font-size: 1.15rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 0.8rem;
        }

        div.stButton > button {
            width: 100%;
            min-height: 85px;
            border: 1px solid #dfe5f0;
            border-radius: 18px;
            background-color: white;
            color: #25304a;
            font-size: 1.25rem;
            font-weight: 800;
            box-shadow: 0 7px 18px rgba(39, 51, 89, 0.08);
            transition:
                transform 0.15s ease,
                box-shadow 0.15s ease,
                border-color 0.15s ease;
        }

        div.stButton > button:hover {
            border-color: #667eea;
            color: #4f5fd5;
            box-shadow: 0 10px 24px rgba(79, 95, 213, 0.18);
            transform: translateY(-3px);
        }

        div.stButton > button:active {
            transform: translateY(0);
        }

        .battle-board {
            display: flex;
            align-items: stretch;
            gap: 14px;
            margin-top: 2rem;
        }

        .choice-card {
            flex: 1;
            padding: 22px 12px;
            border: 1px solid #e1e6ef;
            border-radius: 20px;
            background-color: rgba(255, 255, 255, 0.95);
            box-shadow: 0 8px 24px rgba(34, 45, 78, 0.08);
            color: #26324d;
            text-align: center;
        }

        .choice-owner {
            color: #707b94;
            font-size: 0.9rem;
            font-weight: 800;
        }

        .choice-emoji {
            margin: 10px 0 5px;
            font-size: 3.8rem;
            line-height: 1.1;
        }

        .choice-name {
            color: #17223b;
            font-size: 1.2rem;
            font-weight: 900;
        }

        .versus {
            display: flex;
            align-items: center;
            justify-content: center;
            color: #8992a7;
            font-size: 1rem;
            font-weight: 900;
        }

        .result-card {
            margin-top: 1.2rem;
            padding: 20px;
            border-radius: 20px;
            text-align: center;
            animation: result-pop 0.35s ease-out;
        }

        .result-win {
            border: 1px solid #8bdbb3;
            background: linear-gradient(135deg, #e8fff3, #d8f9e8);
            color: #087a47;
        }

        .result-lose {
            border: 1px solid #ffb5bd;
            background: linear-gradient(135deg, #fff0f2, #ffe1e5);
            color: #b52c3e;
        }

        .result-draw {
            border: 1px solid #a9c9ff;
            background: linear-gradient(135deg, #eef5ff, #dfeaff);
            color: #315ca8;
        }

        .result-title {
            font-size: 1.65rem;
            font-weight: 900;
        }

        .result-message {
            margin-top: 5px;
            font-size: 1rem;
            font-weight: 600;
        }

        .start-card {
            margin-top: 2rem;
            padding: 24px;
            border: 2px dashed #cfd6e5;
            border-radius: 20px;
            color: #758099;
            text-align: center;
        }

        .start-emoji {
            margin-bottom: 5px;
            font-size: 2.4rem;
        }

        .footer {
            margin-top: 2.2rem;
            color: #9199aa;
            font-size: 0.82rem;
            text-align: center;
        }

        @keyframes result-pop {
            0% {
                opacity: 0;
                transform: scale(0.94);
            }

            100% {
                opacity: 1;
                transform: scale(1);
            }
        }

        @media (max-width: 600px) {
            .block-container {
                padding-top: 1.5rem;
            }

            .main-title {
                font-size: 2rem;
            }

            .score-board {
                gap: 7px;
            }

            .score-item {
                min-width: 0;
                flex: 1;
                padding: 10px 6px;
            }

            .battle-board {
                gap: 7px;
            }

            .choice-card {
                padding: 18px 5px;
            }

            .choice-emoji {
                font-size: 3rem;
            }

            .versus {
                font-size: 0.8rem;
            }

            div.stButton > button {
                min-height: 75px;
                font-size: 1.05rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# 제목과 점수판
# --------------------------------------------------
st.markdown(
    '<div class="main-title">✊ 가위바위보 챌린지</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">컴퓨터를 상대로 승리에 도전해 보세요!</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="score-board">
        <div class="score-item">
            <div class="score-label">🏆 승리</div>
            <div class="score-number">{st.session_state.wins}</div>
        </div>

        <div class="score-item">
            <div class="score-label">😅 패배</div>
            <div class="score-number">{st.session_state.losses}</div>
        </div>

        <div class="score-item">
            <div class="score-label">🤝 무승부</div>
            <div class="score-number">{st.session_state.draws}</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# 선택 버튼
# --------------------------------------------------
st.markdown(
    '<div class="section-title">무엇을 내시겠어요?</div>',
    unsafe_allow_html=True,
)

scissors_column, rock_column, paper_column = st.columns(3)

with scissors_column:
    if st.button("✌️ 가위", use_container_width=True):
        play_game("가위")

with rock_column:
    if st.button("✊ 바위", use_container_width=True):
        play_game("바위")

with paper_column:
    if st.button("✋ 보", use_container_width=True):
        play_game("보")


# --------------------------------------------------
# 게임 결과
# --------------------------------------------------
if (
    st.session_state.user_choice is not None
    and st.session_state.computer_choice is not None
):
    user_choice = st.session_state.user_choice
    computer_choice = st.session_state.computer_choice

    st.markdown(
        f"""
        <div class="battle-board">
            <div class="choice-card">
                <div class="choice-owner">나의 선택</div>
                <div class="choice-emoji">{CHOICES[user_choice]}</div>
                <div class="choice-name">{user_choice}</div>
            </div>

            <div class="versus">VS</div>

            <div class="choice-card">
                <div class="choice-owner">컴퓨터의 선택</div>
                <div class="choice-emoji">{CHOICES[computer_choice]}</div>
                <div class="choice-name">{computer_choice}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.result == "win":
        result_class = "result-win"
        result_title = "🎉 승리!"
        result_message = "멋진 선택이에요. 컴퓨터를 이겼습니다!"

    elif st.session_state.result == "lose":
        result_class = "result-lose"
        result_title = "😢 패배!"
        result_message = "아쉽네요. 다시 한번 도전해 보세요!"

    else:
        result_class = "result-draw"
        result_title = "🤝 무승부!"
        result_message = "같은 선택을 했어요. 한 판 더 해볼까요?"

    st.markdown(
        f"""
        <div class="result-card {result_class}">
            <div class="result-title">{result_title}</div>
            <div class="result-message">{result_message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

else:
    st.markdown(
        """
        <div class="start-card">
            <div class="start-emoji">🎮</div>
            가위, 바위, 보 중 하나를 선택하면 게임이 시작됩니다.
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# 기록 초기화
# --------------------------------------------------
st.write("")

reset_column_1, reset_column_2, reset_column_3 = st.columns([1, 1.2, 1])

with reset_column_2:
    st.button(
        "🔄 기록 초기화",
        on_click=reset_game,
        use_container_width=True,
    )

st.markdown(
    '<div class="footer">가위바위보 챌린지 · Streamlit Web App</div>',
    unsafe_allow_html=True,
)
