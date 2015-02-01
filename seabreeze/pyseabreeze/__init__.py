"""This is a wrapper for the pyusb-implementation of the seabreeze-library

"""

# reset connected USB devices
from .wrapper import reset_spectrometers as _reset_spectrometers
_reset_spectrometers()

from .wrapper import (SeaBreezeError,
                      SeaBreezeDevice,
                      list_spectrometers,
                      open_spectrometer,
                      close_spectrometer,
                      get_model,
                      set_trigger_mode,
                      set_integration_time_microsec,
                      get_min_integration_time_microsec,
                      set_shutter_open,
                      get_light_source_count,
                      set_light_source_enable,
                      set_light_source_intensity,
                      read_eeprom_slot,
                      write_eeprom_slot,
                      read_irrad_calibration,
                      write_irrad_calibration,
                      has_irrad_collection_area,
                      read_irrad_collection_area,
                      write_irrad_collection_area,
                      read_tec_temperature,
                      set_tec_temperature,
                      set_tec_enable,
                      set_tec_fan_enable,
                      get_unformatted_spectrum,
                      get_formatted_spectrum,
                      get_unformatted_spectrum_length,
                      get_formatted_spectrum_length,
                      get_wavelengths,
                      get_serial_number,
                      get_electric_dark_pixel_indices,
                      set_continuous_strobe_period_microsec)