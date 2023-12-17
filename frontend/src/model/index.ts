export enum ConversationAuthor {
	GPT = 'gpt',
	USER = 'user',
}

export type Conversation = {
	author: ConversationAuthor;
	message: string;
};
