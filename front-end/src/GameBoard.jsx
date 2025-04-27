import React, { useEffect, useState } from "react";
import axios from "axios";

export default function GameBoard() {
    const [gameState, setGameState] = useState(null);

    useEffect(() => {
        fetchGameState();
    }, []);

    async function fetchGameState() {
        try {
            const response = await axios.get("http://localhost:5000/game-state");
            setGameState(response.data);
        } catch (error) {
            console.error("Error fetching game state", error);
        }
    }

    async function playCard(cardName) {
        try {
            await axios.post("http://localhost:5000/play-card", { cardName });
            await fetchGameState(); // Refresh after playing
        } catch (error) {
            console.error("Error playing card", error);
        }
    }

    if (!gameState) {
        return <div>Loading game...</div>;
    }

    return (
        <div style={styles.board}>
            <div style={styles.topPlayers}>
                {gameState.players.slice(0, 3).map((player, idx) => (
                    <PlayerSlot key={idx} name={player} />
                ))}
            </div>

            <div style={styles.middleArea}>
                <div style={styles.sidePlayer}>
                    <PlayerSlot name={gameState.players[3]} />
                </div>

                <div style={styles.centerArea}>
                    <div style={styles.marketRow}>
                        {gameState.market_cards.map((card, idx) => (
                            <MarketCard key={idx} name={card} />
                        ))}
                    </div>
                </div>

                <div style={styles.sidePlayer}>
                    <PlayerSlot name={gameState.players[4]} />
                </div>
            </div>

            <div style={styles.yourArea}>
                <div style={styles.handArea}>
                    {gameState.your_hand.map((card, idx) => (
                        <HandCard key={idx} name={card} playCard={playCard} />
                    ))}
                </div>
            </div>
        </div>
    );
}

function PlayerSlot({ name }) {
    return <div style={styles.playerSlot}>{name}</div>;
}

function MarketCard({ name }) {
    return <div style={styles.marketCard}>{name}</div>;
}

function HandCard({ name, playCard }) {
    return (
        <div style={styles.handCard} onClick={() => playCard(name)}>
            {name}
        </div>
    );
}

const styles = {
    board: {
        display: "flex",
        flexDirection: "column",
        height: "100vh",
        padding: "10px",
        backgroundColor: "#2e7d32",
    },
    topPlayers: {
        display: "flex",
        justifyContent: "space-around",
        marginBottom: "20px",
    },
    middleArea: {
        display: "flex",
        flex: 1,
        justifyContent: "space-between",
        marginBottom: "20px",
    },
    centerArea: {
        flex: 2,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
    },
    marketRow: {
        display: "flex",
        gap: "10px",
    },
    sidePlayer: {
        flex: 1,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
    },
    yourArea: {
        display: "flex",
        flexDirection: "column",
    },
    handArea: {
        display: "flex",
        justifyContent: "center",
        gap: "10px",
    },
    playerSlot: {
        width: "100px",
        height: "50px",
        backgroundColor: "#aed581",
        borderRadius: "8px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
    },
    marketCard: {
        width: "100px",
        height: "150px",
        backgroundColor: "#90caf9",
        border: "2px solid black",
        borderRadius: "8px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        cursor: "default",
    },
    handCard: {
        width: "100px",
        height: "150px",
        backgroundColor: "#f48fb1",
        border: "2px solid black",
        borderRadius: "8px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        cursor: "pointer",
    },
};
