interface Article {
    title: string;
    subtitle: string;
    description: string;
    createdAt: Date;
    public: boolean;
}

interface ArticlePreview
    extends Omit<Article, "subtitle" | "createdAt" | "public"> {}

const articlePreview: ArticlePreview = {
    title: "TypeScript",
    description: "TS",
};
