import { Conversation, ConversationAuthor } from '../model';

export const ENDPOINT_URL = 'http://localhost:8000/api/';
export const TOAST_LIFE = 7000; // after 7 sec the alert will hide

export const DEFAULT_MESSAGE = [{ author: ConversationAuthor.GPT, message: 'message' }] as Conversation[];
