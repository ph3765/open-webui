<script>
	import { onMount, tick } from 'svelte';
	import { config, user, theme, WEBUI_NAME } from '$lib/stores';
	import { goto } from '$app/navigation';
	import { Toaster, toast } from 'svelte-sonner';

	import { getBackendConfig } from '$lib/apis';
	import { getSessionUser } from '$lib/apis/auths';

	import '../app.css';
	import '../tailwind.css';
	import 'tippy.js/dist/tippy.css';
	import { WEBUI_BASE_URL } from '$lib/constants';

	// 设置国际化
	import {
		_,
		getLocaleFromNavigator,
		isLoading,
		register,
		init,
		locale
	} from "svelte-i18n";

	register("en", () => import("../langs/en.json"));
	register("zh", () => import("../langs/zh.json"));

	init({
    	fallbackLocale: "en",
    	initialLocale: getLocaleFromNavigator()
  	});

	locale.set("zh");

	let loaded = false;

	onMount(async () => {
		theme.set(localStorage.theme);
		// Check Backend Status
		const backendConfig = await getBackendConfig();

		if (backendConfig) {
			// Save Backend Status to Store
			await config.set(backendConfig);

			await WEBUI_NAME.set(backendConfig.name);
			console.log(backendConfig);

			if ($config) {
				if (localStorage.token) {
					// Get Session User Info
					const sessionUser = await getSessionUser(localStorage.token).catch((error) => {
						toast.error(error);
						return null;
					});

					if (sessionUser) {
						// Save Session User to Store
						await user.set(sessionUser);
					} else {
						// Redirect Invalid Session User to /auth Page
						localStorage.removeItem('token');
						await goto('/auth');
					}
				} else {
					await goto('/auth');
				}
			}
		} else {
			// Redirect to /error when Backend Not Detected
			await goto(`/error`);
		}

		await tick();
		loaded = true;
	});
</script>

<svelte:head>
	<title>{$WEBUI_NAME}</title>
	<link rel="icon" href="{WEBUI_BASE_URL}/static/favicon.png" />

	<link rel="stylesheet" type="text/css" href="/themes/rosepine.css" />
	<link rel="stylesheet" type="text/css" href="/themes/rosepine-dawn.css" />
</svelte:head>

{#if loaded}
	<slot />
{/if}

<Toaster richColors position="top-center" />
