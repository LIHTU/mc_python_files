package de.svdragster.antiweather;

import net.canarymod.hook.HookHandler;
import net.canarymod.hook.world.WeatherChangeHook;
import net.canarymod.plugin.PluginListener;

public class AntiWeatherListener implements PluginListener {

	@HookHandler
	public void onWeatherChangeHook(WeatherChangeHook hook) {
		if (hook.turningOn()) {
			hook.setCanceled();
		}
	}
	
}
