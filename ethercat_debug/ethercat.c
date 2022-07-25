/* Master 0, Slave 0
 * Vendor ID:       0x00ecade1
 * Product code:    0x0004d500
 * Revision number: 0x00000001
 */

ec_pdo_entry_info_t slave_0_pdo_entries[] = {
    {0x7200, 0x01, 1}, /* Deactivate */
    {0x7200, 0x02, 1}, /* Activate */
    {0x7200, 0x03, 1}, /* Home */
    {0x7200, 0x04, 1}, /* Reset Error */
    {0x7200, 0x05, 1}, /* Sim Mode */

    {0x7310, 0x01, 16}, /* Move ID */
    {0x7310, 0x02, 1}, /* SetPoint */
    {0x7310, 0x03, 1}, /* Pause */
    {0x7310, 0x04, 1}, /* Clear Move */
    {0x7310, 0x05, 1}, /* Reset PStop */
    
    {0x7305, 0x00, 32}, /* Move Command */
    {0x7306, 0x01, 32}, /* SubIndex 001 */
    {0x7306, 0x02, 32}, /* SubIndex 002 */
    {0x7306, 0x03, 32}, /* SubIndex 003 */
    {0x7306, 0x04, 32}, /* SubIndex 004 */
    {0x7306, 0x05, 32}, /* SubIndex 005 */
    {0x7306, 0x06, 32}, /* SubIndex 006 */
    
    {0x6010, 0x02, 1}, /* Busy */
    {0x6010, 0x03, 1}, /* Activated */
    {0x6010, 0x04, 1}, /* Homed */
    {0x6010, 0x05, 1}, /* SimActivated */
    {0x6010, 0x01, 16}, /* Error */
    
    {0x6015, 0x01, 32}, /* CheckPoint */
    {0x6015, 0x02, 16}, /* Move ID */
    {0x6015, 0x03, 16}, /* FIFO Space */
    {0x6015, 0x04, 1}, /* Paused */
    {0x6015, 0x05, 1}, /* EOB */
    {0x6015, 0x06, 1}, /* EOM */
    {0x6015, 0x07, 1}, /* FIFO Cleared */
    {0x6015, 0x08, 1}, /* PStop */
    {0x6015, 0x09, 1}, /* Excessive torque */
    
    {0x6030, 0x01, 32}, /* SubIndex 001 */
    {0x6030, 0x02, 32}, /* SubIndex 002 */
    {0x6030, 0x03, 32}, /* SubIndex 003 */
    {0x6030, 0x04, 32}, /* SubIndex 004 */
    {0x6030, 0x05, 32}, /* SubIndex 005 */
    {0x6030, 0x06, 32}, /* SubIndex 006 */
    
    {0x6031, 0x01, 32}, /* SubIndex 001 */
    {0x6031, 0x02, 32}, /* SubIndex 002 */
    {0x6031, 0x03, 32}, /* SubIndex 003 */
    {0x6031, 0x04, 32}, /* SubIndex 004 */
    {0x6031, 0x05, 32}, /* SubIndex 005 */
    {0x6031, 0x06, 32}, /* SubIndex 006 */
    
    {0x6032, 0x01, 32}, /* SubIndex 001 */
    {0x6032, 0x02, 32}, /* SubIndex 002 */
    {0x6032, 0x03, 32}, /* SubIndex 003 */
    {0x6032, 0x04, 32}, /* SubIndex 004 */
    {0x6032, 0x05, 32}, /* SubIndex 005 */
    {0x6032, 0x06, 32}, /* SubIndex 006 */
    
    {0x6033, 0x01, 32}, /* SubIndex 001 */
    {0x6033, 0x02, 32}, /* SubIndex 002 */
    {0x6033, 0x03, 32}, /* SubIndex 003 */
    {0x6033, 0x04, 32}, /* SubIndex 004 */
    {0x6033, 0x05, 32}, /* SubIndex 005 */
    {0x6033, 0x06, 32}, /* SubIndex 006 */
    
    {0x6040, 0x01, 32}, /* X */
    {0x6040, 0x02, 32}, /* Y */
    {0x6040, 0x03, 32}, /* Z */
};

ec_pdo_info_t slave_0_pdos[] = {
    {0x1600, 6, slave_0_pdo_entries + 0},   /* Robot Control */
    {0x1601, 6, slave_0_pdo_entries + 5},   /* Motion Control */
    {0x1602, 7, slave_0_pdo_entries + 10},  /* Move */
    {0x1a00, 6, slave_0_pdo_entries + 17},  /* Robot Status */
    {0x1a01, 10, slave_0_pdo_entries + 22}, /* Motion Status */
    {0x1a02, 6, slave_0_pdo_entries + 31},  /* Joint Set */
    {0x1a03, 6, slave_0_pdo_entries + 37},  /* End-Effector Pose */
    {0x1a04, 6, slave_0_pdo_entries + 42},  /* Joint velocities */
    {0x1a05, 6, slave_0_pdo_entries + 49},  /* Torque Ratio */
    {0x1a06, 3, slave_0_pdo_entries + 55},  /* Accelerometer */
};

ec_sync_info_t slave_0_syncs[] = {
    {0, EC_DIR_OUTPUT, 0, NULL, EC_WD_DISABLE},
    {1, EC_DIR_INPUT, 0, NULL, EC_WD_DISABLE},
    {2, EC_DIR_OUTPUT, 3, slave_0_pdos + 0, EC_WD_ENABLE},
    {3, EC_DIR_INPUT, 7, slave_0_pdos + 3, EC_WD_DISABLE},
    {0xff}
};

