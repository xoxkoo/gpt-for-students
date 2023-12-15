<template>
	<Panel class="message-bubble mb-5" :class="`bubble-${author}`" :header="$t(`messages.${author}`)">
		<template #icons> <Button icon="pi pi-bookmark" severity="secondary" rounded text></Button> </template>
		{{ message }}
	</Panel>
</template>
<script setup lang="ts">
import { ConversationAuthor } from '../model';

defineProps({
	author: { type: String as () => ConversationAuthor, required: true },
	message: { type: String, required: true },
});
</script>
