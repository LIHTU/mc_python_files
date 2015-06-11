package de.svdragster.antiweather;

import net.canarymod.Canary;
import net.canarymod.plugin.Plugin;

public class AntiWeather extends Plugin {

	public void disable() {

	}

	public boolean enable() {
		Canary.hooks().registerListener(new AntiWeatherListener(), this);
		return true;
	}

}
