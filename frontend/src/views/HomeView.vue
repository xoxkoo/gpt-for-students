<template>
	<h1 class="text-emerald-700 font-bold text-center mt-20 text-2xl">
		{{ $t('helloWorld') }}
	</h1>

	<Button label="Summarization" icon="pi pi-check" severity="secondary" @click="router.push('summarization')" />
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
const router = useRouter();

console.log(router);
</script>
