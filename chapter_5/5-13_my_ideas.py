# Game title and basic information
title = "ARENA 51: REDACTED"
tagline = "Where Every Experiment Has Consequences"
genre = "Souls-like Sci-Fi / Action RPG / Simulation"
platforms = ["PC", "PlayStation 5", "Xbox Series X|S", "VR Enhanced Edition"]

# Core game design pillars that define the experience
game_pillars = {
    "Challenging Combat": "Pattern-based combat with cosmic horror elements",
    "Deep Conspiracy": "Layered narrative revealed through environment and items",
    "Interconnected World": "Metroidvania-style progression with shortcuts", 
    "Risk-Reward": "Deep progression systems with loss mechanics"
}

# Playable character classes with their abilities and starting equipment
character_classes = {
    "Quantum Researcher": {
        "specialty": "Dimensional manipulation and reality bending",
        "starting_gear": "Quantum Stabilizer, Reality Shard",
        "unique_ability": "Phase Shift"
    },
    # Additional character classes...
}

# Core gameplay systems and mechanics
core_mechanics = {
    "Sanity System": {
        "description": "Mental stability affected by cosmic horror exposure",
        "effects": ["Visual distortions", "Reality breaks", "Temporary madness"]
    },
    # Additional mechanics...
}

# Game world locations and their attributes
locations = {
    "The Mothership": {
        "type": "Central Hub",
        "features": ["Multiple paths", "Vertical design", "Hidden passages"],
        "hazards": ["Reality distortions", "Specimen containment breaches"]
    },
    # Additional locations...
}

# Character progression and advancement systems
progression_systems = {
    "Clearance Levels": {
        "types": ["Alpha", "Beta", "Omega", "Black"],
        "unlocks": "New areas, abilities, and classified information"
    },
    # Additional progression systems...
}

# Multiplayer features and interactions
multiplayer_features = {
    "Invasion System": "Cross-dimensional agent encounters",
    "Co-op Elements": "Joint specimen containment operations",
    "Message System": "Leave classified intel for other players"
}

# Different ending paths and their consequences
endgame_paths = {
    "Full Disclosure": {
        "boss": "The Elder Truth",
        "ending": "Truth Seeker",
        "consequences": "Global paradigm shift"
    },
    # Additional endings...
}

def display_game_design():
    width = 79  # Maximum width for terminal display
    
    sections = [
        ("Game Pillars", game_pillars, "🎮"),
        ("Character Classes", character_classes, "👤"),
        ("Core Mechanics", core_mechanics, "⚙️"),
        ("Locations", locations, "🗺️"),
        ("Progression Systems", progression_systems, "📈"),
        ("Multiplayer Features", multiplayer_features, "👥"),
        ("Endgame Paths", endgame_paths, "🏆")
    ]
    
    # Header section with centered text
    print(f"\n{'='*width}")
    print(f"{f'🔒 {title} 🔒'.center(width)}")
    print(f"{tagline.center(width)}")
    print(f"{'='*width}")
    
    # Genre and platforms left-aligned but respecting max width
    genre_line = f"🎯 Genre: {genre}"
    platform_line = f"🎮 Platforms: {', '.join(platforms)}"
    print(f"\n{genre_line[:width]}")
    print(f"{platform_line[:width]}\n")
    
    for section_name, section_data, icon in sections:
        # Center section headers
        header_text = f"{icon} {section_name.upper()} {icon}"
        print(f"\n{header_text.center(width)}")
        print(f"{'─'*width}")
        
        # Content with proper indentation and width limits
        for key, value in section_data.items():
            print(f"\n▶ {key[:width-2]}")  # -2 for the ▶ and space
            
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, list):
                        print(f"  • {sub_key}:")
                        for item in sub_value:
                            print(f"    ◦ {item[:width-6]}")  # -6 for indent and ◦
                    else:
                        line = f"  • {sub_key}: {sub_value}"
                        print(f"{line[:width]}")
            elif isinstance(value, list):
                for item in value:
                    print(f"  • {item[:width-4]}")  # -4 for indent and •
            else:
                line = f"  • {value}"
                print(f"{line[:width]}")
                
        print(f"\n{'─'*width}")

if __name__ == "__main__":
    display_game_design()
