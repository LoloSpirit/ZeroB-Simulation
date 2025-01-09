simion.workbench_program()
simion.print("Running custom Workbench.lua")

local max_voltage = 3500 -- volts
local rise_time = .1 -- microseconds
local fall_time = .1 -- microseconds
local pulse_duration = 4.5 -- microseconds

local current_voltage = 0

function segment.flym()
    run()
end

--function segment.initialize_run()
    
--end

function segment.fast_adjust()
    -- Calculate the current voltage based on the time of flight (rise -> stay at max for pulse_duration -> fall)
    if ion_time_of_flight < rise_time then
        current_voltage = max_voltage * ion_time_of_flight / rise_time
    elseif ion_time_of_flight < rise_time + pulse_duration then
        current_voltage = max_voltage
    elseif ion_time_of_flight < rise_time + pulse_duration + fall_time then
        current_voltage = max_voltage * (rise_time + pulse_duration + fall_time - ion_time_of_flight) / fall_time
    else
        current_voltage = 0
    end

    adj_elect01 = current_voltage
end

