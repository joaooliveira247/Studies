enum SkillLevel {
    BEGINNER = "beginner",
    INTERMEDIATE = "intermediate",
    ADVANCED = "advanced",
}

interface Resume {
    fullName: string;
    email: string;
    skills: Skill[];
    addSkill: (skill: Skill) => void;
}

interface Skill {
    name: string;
    level: SkillLevel;
}

interface Resume {
    dateOfBirth: Date;
    sumary: string;
}

class MyResume implements Resume {
    constructor(
        public fullName: string,
        public email: string,
        public skills: Skill[]
    ) {}

    public addSkill(skill: Skill): void {
        this.skills.push(skill);
    }
}

const myResume: Resume = new MyResume("John", "john@email.com", [
    { name: "TypeScript", level: SkillLevel.BEGINNER },
    { name: "Go", level: SkillLevel.INTERMEDIATE },
    { name: "JavaScript", level: SkillLevel.BEGINNER },
    { name: "Python", level: SkillLevel.ADVANCED },
]);

console.log(myResume);
myResume.addSkill({ name: "Rust", level: SkillLevel.BEGINNER });
console.log(myResume);
